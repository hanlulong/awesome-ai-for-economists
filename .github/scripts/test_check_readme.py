"""Tests for check_readme.py.

Run: python3 -m unittest discover -s .github/scripts -p 'test_*.py'
"""

import io
import os
import tempfile
import unittest
from contextlib import redirect_stdout
from unittest import mock

import check_readme


def badge(repo):
    return f"![GitHub stars](https://img.shields.io/github/stars/{repo}?style=flat-square)"


CLEAN = f"""# Awesome Example

## Contents

- [Zeta Section](#zeta-section)
- [Alpha Section](#alpha-section)

## Tools

- [alpha](https://github.com/owner/alpha) - Lowercase names sort with the others, ignoring case. {badge("owner/alpha")}
- [**Beta**](https://example.com) - Bold maintainer projects sort by their plain name.
- [Copilot](https://github.com/features/copilot) - A GitHub product page needs no stars badge.
- [Delta](https://delta.example.org) - A website link may carry the badge of its source repository. {badge("owner/delta")}
- [Epsilon](https://github.com/owner/epsilon/tree/main/skills/epsilon) - A link into a subfolder uses the repository's badge. {badge("owner/epsilon")}
- [Zeta](https://github.com/owner/zeta.git) - A .git suffix on the link is ignored. {badge("owner/zeta")}

> - [Highlight](https://example.com) - Blockquote lines are not checked.

### Subsection

- [Aleph](https://example.org/aleph) - A new heading starts a new alphabetical block.

#### Key Papers Group

- [Zebra Paper](https://example.org/zebra) - Author (2026), Venue.
- [Aardvark Paper](https://example.org/aardvark) - Author (2025), Venue.
"""


def problems(text):
    return check_readme.check(text)[0]


def entry_lines(*entries):
    return "# List\n\n## Section\n\n" + "\n".join(entries) + "\n"


class CheckReadmeTest(unittest.TestCase):
    def test_clean_readme_passes(self):
        found, count = check_readme.check(CLEAN)
        self.assertEqual(found, [])
        self.assertEqual(count, 7)

    def test_out_of_order_pair(self):
        found = problems(entry_lines(
            "- [Beta](https://example.com/b) - Second entry.",
            "- [alpha](https://example.com/a) - First entry.",
        ))
        self.assertEqual(len(found), 1)
        line, message = found[0]
        self.assertEqual(line, 6)
        self.assertIn('"alpha" should come before "Beta"', message)

    def test_description_over_twenty_words(self):
        description = " ".join(["word"] * 20) + " last."
        found = problems(entry_lines(
            f"- [Long](https://example.com) - {description} {badge('owner/long')}",
        ))
        self.assertEqual(len(found), 1)
        self.assertIn("21 words", found[0][1])

    def test_twenty_words_with_inline_link_passes(self):
        description = " ".join(["word"] * 17) + " [two words](https://example.com/x) end."
        self.assertEqual(problems(entry_lines(
            f"- [Short](https://example.com) - {description}",
        )), [])

    def test_badge_case_must_match_link(self):
        found = problems(entry_lines(
            f"- [FinBERT](https://github.com/ProsusAI/finBERT) - Sentiment model. {badge('ProsusAI/finbert')}",
        ))
        self.assertEqual(len(found), 1)
        self.assertIn("ProsusAI/finbert", found[0][1])
        self.assertIn("ProsusAI/finBERT", found[0][1])

    def test_github_repository_link_needs_badge(self):
        found = problems(entry_lines(
            "- [Tool](https://github.com/owner/tool) - A tool without a badge.",
        ))
        self.assertEqual(len(found), 1)
        self.assertIn("no stars badge", found[0][1])

    def test_github_product_page_needs_no_badge(self):
        self.assertEqual(problems(entry_lines(
            "- [Copilot](https://github.com/features/copilot) - Coding assistant.",
        )), [])

    def test_contents_and_key_papers_are_ignored(self):
        text = (
            "# List\n\n## Contents\n\n"
            "- [Zeta](#zeta)\n"
            "- [Alpha](#alpha)\n\n"
            "#### Key Papers\n\n"
            "- [Zebra](https://github.com/owner/zebra) - Author (2026), Venue.\n"
            "- [Aardvark](https://example.org/a) - Author (2025), Venue.\n"
        )
        found, count = check_readme.check(text)
        self.assertEqual(found, [])
        self.assertEqual(count, 0)

    def test_duplicate_name(self):
        text = (
            "# List\n\n## One\n\n"
            "- [Tool](https://example.com/a) - First listing.\n\n"
            "## Two\n\n"
            "- [tool](https://example.com/b) - Second listing.\n"
        )
        found = problems(text)
        self.assertEqual(len(found), 1)
        line, message = found[0]
        self.assertEqual(line, 9)
        self.assertIn("also on line 5", message)

    def test_main_exit_codes_and_annotations(self):
        bad = entry_lines("- [Tool](https://github.com/owner/tool) - No badge.")
        with tempfile.TemporaryDirectory() as folder:
            clean_path = os.path.join(folder, "clean.md")
            bad_path = os.path.join(folder, "bad.md")
            with open(clean_path, "w", encoding="utf-8") as handle:
                handle.write(CLEAN)
            with open(bad_path, "w", encoding="utf-8") as handle:
                handle.write(bad)
            with mock.patch.dict(os.environ, {"GITHUB_ACTIONS": "false"}):
                output = io.StringIO()
                with redirect_stdout(output):
                    self.assertEqual(check_readme.main(["check", clean_path]), 0)
                self.assertEqual(output.getvalue(), "OK: 7 entries checked\n")

                output = io.StringIO()
                with redirect_stdout(output):
                    self.assertEqual(check_readme.main(["check", bad_path]), 1)
                self.assertTrue(output.getvalue().startswith(f"{bad_path}:5: "))
            with mock.patch.dict(os.environ, {"GITHUB_ACTIONS": "true"}):
                output = io.StringIO()
                with redirect_stdout(output):
                    self.assertEqual(check_readme.main(["check", bad_path]), 1)
                self.assertTrue(output.getvalue().startswith("::error file="))
                self.assertIn(",line=5::", output.getvalue())


if __name__ == "__main__":
    unittest.main()

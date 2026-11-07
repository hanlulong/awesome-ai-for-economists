#!/usr/bin/env python3
"""Check README.md entries for the format rules that awesome-lint does not cover.

Usage: python3 .github/scripts/check_readme.py [README.md]

Checks each list entry (a line starting with "- [Name](url) - ") for:

- alphabetical order, ignoring case, within its heading block;
- a description of 20 words or fewer, not counting the stars badge;
- a stars badge on every link to a GitHub repository, naming the same
  owner/repo as the link (case-sensitive);
- an entry name that is not already used by another entry.

The Contents block and the Key Papers groups (#### headings) are skipped,
since they follow their own order. Lines that do not match the entry pattern,
such as blockquotes and Community lines, are left to awesome-lint, as are
punctuation, capitalization, and duplicate links.

Prints one line per problem and exits 1, or prints "OK: <n> entries checked"
and exits 0. Inside GitHub Actions, problems are printed as error annotations.
"""

import os
import re
import sys

MAX_WORDS = 20

ENTRY_RE = re.compile(
    r"^- \[(\*\*)?(?P<name>.+?)(\*\*)?\]\((?P<url>[^)\s]+)\) - (?P<desc>.+)$"
)
BADGE_RE = re.compile(
    r"!\[GitHub stars\]\(https://img\.shields\.io/github/stars/"
    r"(?P<repo>[^?)\s]+)\?style=flat-square\)\s*$"
)
LINK_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")
GITHUB_RE = re.compile(r"^https://github\.com/(?P<owner>[^/#?]+)/(?P<repo>[^/#?]+)")

# github.com paths whose first segment is a GitHub page, not a repository owner.
NOT_OWNERS = {
    "features", "orgs", "topics", "sponsors", "marketplace", "settings", "apps",
    "collections", "enterprise", "about", "pricing", "login", "users",
}


def check(text):
    """Return (problems, entry_count); problems is a list of (line, message)."""
    problems = []
    first_seen = {}  # casefolded name -> line number
    count = 0
    heading = ""
    skip = False
    previous = None  # name of the previous entry in the current block

    for number, line in enumerate(text.split("\n"), 1):
        if line.startswith("#"):
            heading = line.lstrip("#").strip()
            skip = line.strip() == "## Contents" or line.startswith("####")
            previous = None
            continue
        if skip or not line.startswith("- ["):
            continue
        match = ENTRY_RE.match(line)
        if not match:
            continue
        count += 1
        name, url, desc = match.group("name", "url", "desc")
        key = name.casefold()

        if previous is not None and key < previous.casefold():
            problems.append((
                number,
                f'"{name}" should come before "{previous}" '
                f'(alphabetical order, ignoring case, in "{heading}")',
            ))
        previous = name

        badge = BADGE_RE.search(desc)
        body = desc[: badge.start()] if badge else desc
        words = len(LINK_RE.sub(r"\1", body).split())
        if words > MAX_WORDS:
            problems.append((
                number,
                f'"{name}" description has {words} words (limit {MAX_WORDS})',
            ))

        github = GITHUB_RE.match(url)
        if github and github.group("owner").lower() not in NOT_OWNERS:
            repo_name = github.group("repo")
            if repo_name.endswith(".git"):
                repo_name = repo_name[: -len(".git")]
            repo = f'{github.group("owner")}/{repo_name}'
            if not badge:
                problems.append((
                    number,
                    f'"{name}" links to the GitHub repository {repo} '
                    f"but has no stars badge",
                ))
            elif badge.group("repo") != repo:
                problems.append((
                    number,
                    f'"{name}" stars badge names {badge.group("repo")}, '
                    f"but the link points to {repo} (they must match exactly)",
                ))

        if key in first_seen:
            problems.append((
                number,
                f'"{name}" is listed twice (also on line {first_seen[key]})',
            ))
        else:
            first_seen[key] = number

    problems.sort(key=lambda problem: problem[0])
    return problems, count


def escape_data(value):
    return value.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")


def escape_property(value):
    return escape_data(value).replace(":", "%3A").replace(",", "%2C")


def main(argv):
    path = argv[1] if len(argv) > 1 else "README.md"
    with open(path, encoding="utf-8") as handle:
        problems, count = check(handle.read())
    annotate = os.environ.get("GITHUB_ACTIONS") == "true"
    for number, message in problems:
        if annotate:
            print(f"::error file={escape_property(path)},line={number}::"
                  f"{escape_data(message)}")
        else:
            print(f"{path}:{number}: {message}")
    if problems:
        return 1
    print(f"OK: {count} entries checked")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

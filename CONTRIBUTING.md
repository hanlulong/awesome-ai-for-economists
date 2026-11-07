# Contributing to Awesome AI for Economists

Thank you for helping improve this list. It collects AI tools and resources with specific value for economists, plus research on the economics of AI. Every suggestion is reviewed against the criteria below.

## Quick Start

1. **Fork** this repository.
2. **Add one resource** to the right section of `README.md`.
3. **Open a pull request** and fill in the template, including your affiliation.

Not sure whether a resource fits, or where it goes? Open an [issue](https://github.com/hanlulong/awesome-ai-for-economists/issues) first.

## Entry Format

Use this exact format:

```markdown
- [Name](https://example.com) - One-sentence description ending with a period. ![GitHub stars](https://img.shields.io/github/stars/owner/repo?style=flat-square)
```

- Use the project's official name as the link text. Link its own website or upstream repository, never a fork, mirror, directory, marketplace, or news article.
- Write one objective sentence of 20 words or fewer that starts with a capital letter and ends with a period. Leave out superlatives, marketing claims, usage counts, and prices.
- Avoid wording that goes out of date, such as submission deadlines.
- Add the stars badge whenever the project's source code is on GitHub, even if the link points to its website. The badge's `owner/repo` must match the repository's current name.
- Place the entry in alphabetical order (ignoring case) within its section. Key Papers are the one exception (see the next point).
- Key Papers use `- [Full official title](https://example.com) - Authors (Year), Venue.` Name up to three authors, and write "First author et al." for four or more. Papers are grouped by theme and listed newest first, then by first author.
- Books, Conferences, and Community follow their own patterns. Books name the authors and topic and end with `(Publisher, Year)` when formally published. Conferences name the organizer and give the place and dates of the latest or next meeting, such as `(latest: Cornell, June 16–17, 2026)`. Community lines separate `[Name](https://example.com)` items with ` | `, add the author or institution in parentheses where useful, and sort by name (People by surname).
- Do not use bold. Bold marks the maintainers' own projects (see below).
- Pull requests are checked with awesome-lint and `.github/scripts/check_readme.py`, and both checks must pass before merging. For first-time contributors, the checks run once a maintainer approves the workflow run.
- To check your change before opening a pull request, run `npx awesome-lint@2.3.0 README.md` and `python3 .github/scripts/check_readme.py README.md`. In a fork, errors from awesome-lint's `remark-lint:awesome-github` rule (missing "awesome" or "awesome-list" topics, or "Awesome list must reside in a valid git repository" before your branch is pushed) come from the fork's setup and can be ignored; fix every other error.

## Pull Request Rules

- **One resource per pull request.** Add one line and change nothing else.
- **Disclose your affiliation.** If you built, work for, or are paid by the project, say so in the pull request. Affiliated submissions are welcome and are held to the same standard.
- Fixes to existing entries, such as a broken link or an outdated description, are welcome in separate pull requests.
- Pull requests that edit unrelated lines, add several resources, or repeat an open pull request will be closed.

## Inclusion Criteria

A new resource must meet each criterion that applies to it:

- **Relevance.** It has specific value for economic research, teaching, or policy analysis, or it is research on the economics of AI.
- **Traction.** Software needs at least 50 GitHub stars, an institutional maintainer (such as a statistical agency, central bank, international organization, university lab, or journal), or use in published research. Agent skills need at least 20 stars or institutional authorship. MCP servers follow the MCP rules below instead.
- **Credible authorship.** Papers appear in a reputable venue or as working papers from a recognized institution (NBER, CEPR, and similar). Courses and guides come from recognized researchers, instructors, or institutions.
- **Free access.** It is open source, free, or has a free tier or academic access that supports real research use. A short trial or a handful of free queries does not count, and pay-per-call-only services do not qualify.
- **Maintenance.** New submissions must have been updated in the last 12 months. Listed projects are removed when they are archived or go two years without updates. Models, datasets, and replication code released with a peer-reviewed paper are exempt from both update rules while they still work and no maintained tool does the same job.

### MCP Servers

The MCP section lists servers for economic, financial, or official statistical data used in research. A server qualifies if:

- It is the data provider's official server, or it covers a data source or capability that no listed server covers.
- It is open source with install instructions, or hosted with a free tier and public documentation.
- It was updated in the last 12 months.

Servers that mainly sell access to a commercial market-data API, serve trading signals or crypto data, or charge per call are out of scope. If an official server exists for a source, a community server for the same source must offer something the official one lacks, such as self-hosting.

### Agent Skills

The Agent Skills section lists repositories whose main deliverable is installable skills (`SKILL.md` files) built for economics work, such as econometrics, Stata or Dynare, journal standards, replication, or refereeing.

- A library, CLI, MCP server, or guide that also ships a skill stays in its task section and mentions the skill in its description.
- The skill has a readable `SKILL.md` in a public repository. If it sits in a subfolder of a larger repository, link the folder.
- Link the original repository, never a fork, mirror, or re-bundle. Directories that collect other people's skills are not listed.
- General-purpose skill packs go on the section's "More skills" line, not in the list.
- For a personal kit, name the author and institution, for example "Scott Cunningham's (Baylor)".
- Mention non-commercial or other restrictive license terms in the description.
- Reviewers read the `SKILL.md` before merging. Skills built to evade AI-text detection or plagiarism checks are rejected.

## What We Are Looking For

- AI tools and libraries for economic research, teaching, or policy analysis.
- Libraries for econometrics, causal inference, forecasting, and economic modeling.
- MCP servers and agent skills built for economics work.
- Benchmarks of AI on economic tasks, and trackers of AI adoption and its economic effects.
- Papers, books, courses, and guides on AI and economics.

## What We Are Not Looking For

- General-purpose AI tools with no specific relevance to economics. A few widely used assistants and coding agents are listed in the Appendix, which the maintainers curate.
- Paid tools without a free tier or academic access, and pay-per-call-only services.
- Retail investing products, trading-signal services, and crypto tools.
- Archived or abandoned projects, and duplicates of listed resources.
- Forks, mirrors, and re-packaged copies of other projects.

## Maintainer Projects

Projects by the OpenEcon team, which maintains this list, are marked in **bold** and repeated in the Highlights block at the top. Each is listed once in its best-fit section and follows the same format rules. Newer team projects may be listed before they reach the traction bar; the bold marking makes that visible.

## Suggesting a New Section

If a resource does not fit any existing section, open an issue to discuss whether a new section is warranted.

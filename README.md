# Awesome AI for Economists [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://makeapullrequest.com)
[![Last Commit](https://img.shields.io/github/last-commit/hanlulong/awesome-ai-for-economists)](https://github.com/hanlulong/awesome-ai-for-economists/commits/main)

A curated list of AI tools, agent skills, libraries, and resources for economics research, teaching, and policy analysis.

> **Scope:** AI tools and resources with specific value for economists, plus research on the economics of AI. General-purpose AI assistants and coding agents are in the Appendix.

<!-- Highlights repeats the team's own entries on purpose. Its reference-style links are not counted by awesome-lint's double-link check, which stays strict for every inline link below. -->
> **Highlights:** Projects from the [OpenEcon](https://openecon.ai/) team, which maintains this list. Entries in **bold** below are the team's own.
>
> - [**AI-research-setup**][ai-research-setup] - Step-by-step guide to setting up Claude Code and Codex for economics research on macOS and Windows. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/AI-research-setup?style=flat-square)
> - [**OpenEcon Data**][openecon-data] - MCP server and web app for plain-English queries over 330,000+ indicators from FRED, World Bank, IMF, Eurostat, and more. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/openecon-data?style=flat-square)
> - [**Stata-MCP**][stata-mcp] - Runs Stata from VS Code, Cursor, Claude Code, Codex, and Copilot with real-time output, a data viewer, and graph display. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/stata-mcp?style=flat-square)
> - [**Econ Writing Skill**][econ-writing-skill] - Economics paper-writing skill synthesizing 50+ guides by Cochrane, McCloskey, Shapiro, Head, and others. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/econ-writing-skill?style=flat-square)
> - [**Econ Paper Review Skill**][econ-paper-review-skill] - Writes referee reports on economics papers with verified comments, editing notes, and a step-by-step revision plan; free for non-commercial use. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/econ-paper-review-skill?style=flat-square)
> - [**Econ Slides Skill**][econ-slides-skill] - Turns a paper into a Beamer talk with a timed speaker script, including job-market and discussant decks. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/econ-slides-skill?style=flat-square)
> - [**overleaf-sync-now**][overleaf-sync-now] - Agent skill and CLI that pull recent Overleaf web edits into a Dropbox-synced copy before AI agents edit it. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/overleaf-sync-now?style=flat-square)
> - [**Econ Auto Research**][econ-auto-research] - Vision-stage plan (no code yet) for an economist-directed AI pipeline from research question to working paper, with adversarial self-refereeing. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/econ-auto-research?style=flat-square)
>
> [ai-research-setup]: https://github.com/hanlulong/AI-research-setup
> [openecon-data]: https://github.com/hanlulong/openecon-data
> [stata-mcp]: https://github.com/hanlulong/stata-mcp
> [econ-writing-skill]: https://github.com/hanlulong/econ-writing-skill
> [econ-paper-review-skill]: https://github.com/hanlulong/econ-paper-review-skill
> [econ-slides-skill]: https://github.com/hanlulong/econ-slides-skill
> [overleaf-sync-now]: https://github.com/hanlulong/overleaf-sync-now
> [econ-auto-research]: https://github.com/hanlulong/econ-auto-research

## Contents

- [MCP Servers for Economic Data](#mcp-servers-for-economic-data)
- [Agent Skills for Economists](#agent-skills-for-economists)
- [Coding Tools for Economists](#coding-tools-for-economists)
- [AI Agents for Research](#ai-agents-for-research)
- [Causal Inference and Econometrics](#causal-inference-and-econometrics)
- [Simulation, Forecasting and Macro Modeling](#simulation-forecasting-and-macro-modeling)
- [Literature Review and Research Discovery](#literature-review-and-research-discovery)
- [Economic Data and Analysis](#economic-data-and-analysis)
- [Academic Writing and LaTeX](#academic-writing-and-latex)
- [Document Processing and OCR](#document-processing-and-ocr)
- [NLP and Text as Data](#nlp-and-text-as-data)
- [Policy, Labor and Alternative Data](#policy-labor-and-alternative-data)
- [Finance-Specific AI](#finance-specific-ai)
- [Data Collection Tools](#data-collection-tools)
- [Benchmarks and Evaluation](#benchmarks-and-evaluation)
- [Papers and Books](#papers-and-books)
- [Courses, Conferences and Community](#courses-conferences-and-community)
- [Appendix: General-Purpose AI](#appendix-general-purpose-ai)

## MCP Servers for Economic Data

[Model Context Protocol](https://modelcontextprotocol.io/) (MCP) servers let AI assistants query economic databases directly. Connect Claude, Cursor, or other MCP-compatible tools to live data from FRED, World Bank, IMF, and more.

- [Alpha Vantage MCP](https://mcp.alphavantage.co/) - Official server for stocks, forex, commodities, and economic indicators.
- [Data Commons MCP Server](https://github.com/datacommonsorg/agent-toolkit) - Official Data Commons server, hosted with a free key or run locally, serving Census, World Bank, BLS, and WHO statistics. ![GitHub stars](https://img.shields.io/github/stars/datacommonsorg/agent-toolkit?style=flat-square)
- [ECB MCP Server](https://github.com/scka-de/ecb-mcp) - Query European Central Bank exchange rates, policy rates, yield curves, and euro-area monetary statistics. ![GitHub stars](https://img.shields.io/github/stars/scka-de/ecb-mcp?style=flat-square)
- [Equibles MCP](https://github.com/daniel3303/Equibles) - Self-hosted, open-source server for SEC filings, XBRL financials, 13F holdings, insider trades, short interest, CFTC positioning, and federal contracts. ![GitHub stars](https://img.shields.io/github/stars/daniel3303/Equibles?style=flat-square)
- [Eurostat MCP Server](https://github.com/cyanheads/eurostat-mcp-server) - Search, inspect, and query Eurostat datasets, including Comext detailed trade, PRODCOM, and NUTS regional data. ![GitHub stars](https://img.shields.io/github/stars/cyanheads/eurostat-mcp-server?style=flat-square)
- [FRED MCP Connector](https://fred.stlouisfed.org/help/data/connecting-fred-to-ai-services/fred-mcp-connector) - St. Louis Fed's official connector letting AI assistants search, fetch, and chart FRED series; requires only a free account.
- [FRED MCP Server](https://github.com/stefanoamorelli/fred-mcp-server) - Community open-source FRED server run with your own free API key; a self-hostable alternative to the official connector. ![GitHub stars](https://img.shields.io/github/stars/stefanoamorelli/fred-mcp-server?style=flat-square)
- [IMF Data MCP Server](https://github.com/c-cf/imf-data-mcp) - WEO forecasts, balance of payments, and more from the IMF. ![GitHub stars](https://img.shields.io/github/stars/c-cf/imf-data-mcp?style=flat-square)
- [Invokely](https://invokely.ai/docs) - Hosted server for official U.S., EU, UK, Canadian, and Australian statistics, down to U.S. counties and Spanish municipalities.
- [MoSPI eSankhyiki MCP](https://github.com/nso-india/esankhyiki-mcp) - Official Indian statistics ministry server for PLFS, CPI, national accounts, NSS surveys, and more. ![GitHub stars](https://img.shields.io/github/stars/nso-india/esankhyiki-mcp?style=flat-square)
- [Nasdaq Data Link MCP](https://github.com/stefanoamorelli/nasdaq-data-link-mcp) - Access Nasdaq/Quandl financial and economic datasets. ![GitHub stars](https://img.shields.io/github/stars/stefanoamorelli/nasdaq-data-link-mcp?style=flat-square)
- [OECD MCP Server](https://github.com/isakskogstad/OECD-MCP) - Access 5,000+ OECD statistical datasets via SDMX API with prompt templates. ![GitHub stars](https://img.shields.io/github/stars/isakskogstad/OECD-MCP?style=flat-square)
- [**OpenEcon Data**](https://github.com/hanlulong/openecon-data) - MCP server and web app for plain-English queries over 330,000+ indicators from FRED, World Bank, IMF, Eurostat, and more. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/openecon-data?style=flat-square)
- [SEC EDGAR MCP](https://github.com/stefanoamorelli/sec-edgar-mcp) - Connects AI assistants to U.S. SEC EDGAR filings, financial statements, and insider-trading data. ![GitHub stars](https://img.shields.io/github/stars/stefanoamorelli/sec-edgar-mcp?style=flat-square)
- [StatCite](https://statcite.com) - World Bank, IMF, and ECB statistics where every value carries a full citation, plus verification of claimed figures. ![GitHub stars](https://img.shields.io/github/stars/asokore/statcite?style=flat-square)
- [StatOrigin](https://statorigin.org/docs/mcp) - Free remote MCP for industry statistics; every figure links to its publisher, report and source sentence. No API key. ![GitHub stars](https://img.shields.io/github/stars/SudoAI-App/statorigin-mcp?style=flat-square)
- [U.S. Census Bureau Data API MCP](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp) - Official Census Bureau server connecting AI assistants to demographic, economic, and population statistics. ![GitHub stars](https://img.shields.io/github/stars/uscensusbureau/us-census-bureau-data-api-mcp?style=flat-square)
- [UN Comtrade MCP Server](https://github.com/cyanheads/un-comtrade-mcp-server) - Access UN Comtrade international trade statistics with country and HS commodity code lookup. ![GitHub stars](https://img.shields.io/github/stars/cyanheads/un-comtrade-mcp-server?style=flat-square)
- [World Bank Data360 MCP](https://github.com/worldbank/data360-mcp) - Official World Bank server with a public hosted endpoint (no key needed) for searching, fetching, and charting Data360 indicators. ![GitHub stars](https://img.shields.io/github/stars/worldbank/data360-mcp?style=flat-square)
- [World Bank MCP Server](https://github.com/anshumax/world_bank_mcp_server) - Community server for the legacy World Bank Open Data API (the official one is World Bank Data360 MCP above). ![GitHub stars](https://img.shields.io/github/stars/anshumax/world_bank_mcp_server?style=flat-square)

> Browse the [MCP Registry](https://registry.modelcontextprotocol.io/) to discover more servers.

## Agent Skills for Economists

[Agent Skills](https://agentskills.io/) are folders that an AI agent loads when a task needs them: a `SKILL.md` file of instructions, plus optional scripts and reference files. The open format works in Claude, Claude Code, OpenAI Codex, GitHub Copilot, Cursor, and other agents.

- [AI Research Feedback](https://github.com/claesbackman/AI-research-feedback) - Claes Bäckman's (SAFE Frankfurt) skills for multi-agent referee reports plus pre-analysis-plan, grant, and replication-code reviews. ![GitHub stars](https://img.shields.io/github/stars/claesbackman/AI-research-feedback?style=flat-square)
- [Awesome Journal Skills](https://github.com/brycewang-stanford/Awesome-Journal-Skills) - Per-journal skill packs for AER, QJE, the AEJs, and hundreds of other venues, from topic choice to referee response. ![GitHub stars](https://img.shields.io/github/stars/brycewang-stanford/Awesome-Journal-Skills?style=flat-square)
- [awesome-econ-ai-stuff](https://github.com/meleantonio/awesome-econ-ai-stuff) - Antonio Mele's (LSE) SKILL.md collection for Stata, R, and Python econometrics, data fetching, LaTeX tables, literature review, and modeling. ![GitHub stars](https://img.shields.io/github/stars/meleantonio/awesome-econ-ai-stuff?style=flat-square)
- [Claude Code Academic Workflow](https://github.com/pedrohcgs/claude-code-my-workflow) - Pedro Sant'Anna's (Emory) ready-to-fork template with 60+ skills, multi-agent review, quality gates, and replication protocols. ![GitHub stars](https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat-square)
- [dynare-copilot](https://github.com/EconSolider/dynare-copilot) - Skill turning macro model ideas into validated Dynare .mod files, drawing on 149 Macroeconomic Model Data Base models. ![GitHub stars](https://img.shields.io/github/stars/EconSolider/dynare-copilot?style=flat-square)
- [**Econ Paper Review Skill**](https://github.com/hanlulong/econ-paper-review-skill) - Writes referee reports on economics papers with verified comments, editing notes, and a step-by-step revision plan; free for non-commercial use. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/econ-paper-review-skill?style=flat-square)
- [**Econ Slides Skill**](https://github.com/hanlulong/econ-slides-skill) - Turns a paper into a Beamer talk with a timed speaker script, including job-market and discussant decks. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/econ-slides-skill?style=flat-square)
- [**Econ Writing Skill**](https://github.com/hanlulong/econ-writing-skill) - Economics paper-writing skill synthesizing 50+ guides by Cochrane, McCloskey, Shapiro, Head, and others. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/econ-writing-skill?style=flat-square)
- [MixtapeTools](https://github.com/scunning1975/MixtapeTools) - Scott Cunningham's (Baylor) skills for independent code audits, cross-language replication, bibliography checks, and Beamer decks. ![GitHub stars](https://img.shields.io/github/stars/scunning1975/MixtapeTools?style=flat-square)
- [Stata Skill](https://github.com/dylantmoore/stata-skill) - Dylan Moore's (Hawaii) Stata reference skill covering econometrics, causal inference, Mata, and 20+ community packages such as reghdfe. ![GitHub stars](https://img.shields.io/github/stars/dylantmoore/stata-skill?style=flat-square)
- [World Bank Reproducibility Skill](https://github.com/worldbank/wb-reproducible-research-repository/tree/main/ai-skills/reproducibility-skill) - Official World Bank skill that audits and assembles replication packages, starting with a data-privacy check. ![GitHub stars](https://img.shields.io/github/stars/worldbank/wb-reproducible-research-repository?style=flat-square)

> **More skills:** [Academic Research Skills](https://github.com/Imbad0202/academic-research-skills) (research-to-publication pipeline, CC BY-NC) | [Anthropic Skills](https://github.com/anthropics/skills) (Word, Excel, PowerPoint, PDF) | [Posit Skills](https://github.com/posit-dev/skills) (Quarto, tidyverse, Shiny) | [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) (statistics, FRED and World Bank lookups). Browse [skills.sh](https://skills.sh/) for more. Skills can run code on your computer, so read a third-party skill's `SKILL.md` and scripts before installing it.

## Coding Tools for Economists

_AI assistants, agent connectors, and setup guides for Stata, R, MATLAB, Python, and notebooks. General-purpose coding agents are in the Appendix._

- [**AI-research-setup**](https://github.com/hanlulong/AI-research-setup) - Step-by-step guide to setting up Claude Code and Codex for economics research on macOS and Windows. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/AI-research-setup?style=flat-square)
- [Jupyter AI](https://github.com/jupyterlab/jupyter-ai) - Official JupyterLab extension bringing Claude, Codex, Gemini, and other agents into notebooks through a chat panel. ![GitHub stars](https://img.shields.io/github/stars/jupyterlab/jupyter-ai?style=flat-square)
- [Jupyter MCP Server](https://github.com/datalayer/jupyter-mcp-server) - MCP server and Claude Code plugin letting AI agents edit and run live Jupyter notebooks. ![GitHub stars](https://img.shields.io/github/stars/datalayer/jupyter-mcp-server?style=flat-square)
- [marimo](https://github.com/marimo-team/marimo) - Reactive Python notebook stored as pure .py files with built-in AI assistant. ![GitHub stars](https://img.shields.io/github/stars/marimo-team/marimo?style=flat-square)
- [MATLAB MCP Server](https://github.com/matlab/matlab-mcp-server) - Official MathWorks server letting Claude Code, Codex, and Copilot run, lint, and test code in your local MATLAB. ![GitHub stars](https://img.shields.io/github/stars/matlab/matlab-mcp-server?style=flat-square)
- [MCP-for-Stata](https://github.com/SepineTam/mcp-for-stata) - MCP server and CLI, with bundled Stata skills, letting Claude Code, Codex, and other agents run local Stata. ![GitHub stars](https://img.shields.io/github/stars/SepineTam/mcp-for-stata?style=flat-square)
- [mcptools](https://github.com/posit-dev/mcptools) - Posit's R package letting Claude Code, Copilot, and other MCP clients run code in your live R sessions. ![GitHub stars](https://img.shields.io/github/stars/posit-dev/mcptools?style=flat-square)
- [Posit Assistant](https://assistant.posit.co/) - Posit's data-analysis agent for RStudio, Positron, and the terminal, working in live R and Python sessions with major model providers.
- [Positron](https://positron.posit.co/) - Free Posit data science IDE for R and Python, with the Posit Assistant agent built in. ![GitHub stars](https://img.shields.io/github/stars/posit-dev/positron?style=flat-square)
- [**Stata-MCP**](https://github.com/hanlulong/stata-mcp) - Runs Stata from VS Code, Cursor, Claude Code, Codex, and Copilot with real-time output, a data viewer, and graph display. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/stata-mcp?style=flat-square)

## AI Agents for Research

### AI Agent Frameworks

_Libraries for building your own LLM pipelines and agents, from data collection to analysis and reporting._

- [Agno](https://github.com/agno-agi/agno) - Open-source Python framework with memory, knowledge, and 100+ toolkits including MCP support. ![GitHub stars](https://img.shields.io/github/stars/agno-agi/agno?style=flat-square)
- [chatlas](https://posit-dev.github.io/chatlas/) - Posit's Python interface for LLMs with streaming, tool calling, and structured output. ![GitHub stars](https://img.shields.io/github/stars/posit-dev/chatlas?style=flat-square)
- [CrewAI](https://github.com/crewAIInc/crewAI) - Open-source Python framework for orchestrating role-based, collaborative multi-agent systems. ![GitHub stars](https://img.shields.io/github/stars/crewAIInc/crewAI?style=flat-square)
- [DSPy](https://github.com/stanfordnlp/dspy) - Stanford NLP framework for building LLM pipelines from declarative Python modules, with optimizers that tune prompts and weights. ![GitHub stars](https://img.shields.io/github/stars/stanfordnlp/dspy?style=flat-square)
- [ellmer](https://ellmer.tidyverse.org) - Tidyverse R package for calling LLM APIs with tool calling and structured data extraction. ![GitHub stars](https://img.shields.io/github/stars/tidyverse/ellmer?style=flat-square)
- [Google ADK](https://github.com/google/adk-python) - Google's modular multi-agent framework with MCP and A2A protocol support. ![GitHub stars](https://img.shields.io/github/stars/google/adk-python?style=flat-square)
- [LangGraph](https://github.com/langchain-ai/langgraph) - LangChain's low-level framework for stateful, durable agent workflows built as graphs. ![GitHub stars](https://img.shields.io/github/stars/langchain-ai/langgraph?style=flat-square)
- [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) - Microsoft's successor to AutoGen and Semantic Kernel for multi-agent workflows in Python and .NET. ![GitHub stars](https://img.shields.io/github/stars/microsoft/agent-framework?style=flat-square)
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - Lightweight Python framework for multi-agent workflows with handoffs, guardrails, and tracing. ![GitHub stars](https://img.shields.io/github/stars/openai/openai-agents-python?style=flat-square)
- [Pydantic AI](https://github.com/pydantic/pydantic-ai) - Type-safe Python agent framework with validated structured outputs across all major model providers. ![GitHub stars](https://img.shields.io/github/stars/pydantic/pydantic-ai?style=flat-square)
- [smolagents](https://github.com/huggingface/smolagents) - Hugging Face's minimalist agent library where agents write actions as Python code. ![GitHub stars](https://img.shields.io/github/stars/huggingface/smolagents?style=flat-square)

### Autonomous Research Agents

_Systems that turn a research question into a cited report, an analysis, or a draft paper._

- [DeerFlow](https://github.com/bytedance/deer-flow) - ByteDance's research SuperAgent for long-horizon tasks with sandboxed code execution. ![GitHub stars](https://img.shields.io/github/stars/bytedance/deer-flow?style=flat-square)
- [**Econ Auto Research**](https://github.com/hanlulong/econ-auto-research) - Vision-stage plan (no code yet) for an economist-directed AI pipeline from research question to working paper, with adversarial self-refereeing. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/econ-auto-research?style=flat-square)
- [GPT Researcher](https://github.com/assafelovic/gpt-researcher) - Autonomous deep research agent producing cited reports from web sources. ![GitHub stars](https://img.shields.io/github/stars/assafelovic/gpt-researcher?style=flat-square)
- [Kosmos](https://edisonscientific.com/) - Edison Scientific's AI scientist that reads literature, analyzes datasets, and generates hypotheses in long autonomous runs.
- [Project APE](https://ape.socialcatalystlab.org) - University of Zurich experiment in which AI agents wrote 1,000 open policy-evaluation papers, ranked by LLM judges against AER/AEJ papers. ![GitHub stars](https://img.shields.io/github/stars/SocialCatalystLab/ape-papers?style=flat-square)
- [The AI Scientist](https://github.com/SakanaAI/AI-Scientist) - Sakana AI system that generates ML research ideas, runs experiments, and writes and reviews LaTeX papers (Nature 2026; template-free [v2](https://github.com/SakanaAI/AI-Scientist-v2)). ![GitHub stars](https://img.shields.io/github/stars/SakanaAI/AI-Scientist?style=flat-square)

## Causal Inference and Econometrics

### Core Libraries

- [awesome-causal-inference](https://github.com/matteocourthoud/awesome-causal-inference) - Curated list of causal inference resources, courses, and tools. ![GitHub stars](https://img.shields.io/github/stars/matteocourthoud/awesome-causal-inference?style=flat-square)
- [causal-learn](https://github.com/py-why/causal-learn) - Causal discovery algorithms (PC, FCI, GES) from the PyWhy ecosystem. ![GitHub stars](https://img.shields.io/github/stars/py-why/causal-learn?style=flat-square)
- [CausalMatch](https://github.com/bytedance/CausalMatch) - ByteDance's Python package for propensity score matching and coarsened exact matching, with machine-learning propensity models. ![GitHub stars](https://img.shields.io/github/stars/bytedance/CausalMatch?style=flat-square)
- [CausalML](https://github.com/uber/causalml) - Uber's uplift modeling and causal inference with machine learning. ![GitHub stars](https://img.shields.io/github/stars/uber/causalml?style=flat-square)
- [CausalPy](https://github.com/pymc-labs/CausalPy) - Bayesian causal inference for quasi-experiments (DiD, synthetic control, RDD) powered by PyMC, with bundled agent skills. ![GitHub stars](https://img.shields.io/github/stars/pymc-labs/CausalPy?style=flat-square)
- [ddml](https://github.com/aahrens1/ddml) - Double/debiased ML with stacked learners for Stata (Ahrens, Hansen, Schaffer, Wiemann), with a sister R package. ![GitHub stars](https://img.shields.io/github/stars/aahrens1/ddml?style=flat-square)
- [DoubleML](https://docs.doubleml.org/) - Double/debiased ML (Chernozhukov et al., 2018) in Python and R; the Python package adds DiD, RDD, and panel fixed-effects models. ![GitHub stars](https://img.shields.io/github/stars/DoubleML/doubleml-for-py?style=flat-square)
- [DoWhy](https://github.com/py-why/dowhy) - End-to-end causal inference: model, identify, estimate, refute. ![GitHub stars](https://img.shields.io/github/stars/py-why/dowhy?style=flat-square)
- [EconML](https://github.com/py-why/EconML) - Microsoft/PyWhy library for heterogeneous treatment effects via Double ML and causal forests. ![GitHub stars](https://img.shields.io/github/stars/py-why/EconML?style=flat-square)
- [grf](https://github.com/grf-labs/grf) - Generalized Random Forests for heterogeneous treatment effects (Athey, Tibshirani, Wager). ![GitHub stars](https://img.shields.io/github/stars/grf-labs/grf?style=flat-square)
- [marginaleffects](https://github.com/vincentarelbundock/marginaleffects) - Predictions, slopes, marginal means, and contrasts for 100+ model classes in R and Python, with an official agent skill. ![GitHub stars](https://img.shields.io/github/stars/vincentarelbundock/marginaleffects?style=flat-square)
- [policytree](https://github.com/grf-labs/policytree) - R package for learning shallow-tree treatment-assignment rules via doubly robust empirical welfare maximization (Athey and Wager). ![GitHub stars](https://img.shields.io/github/stars/grf-labs/policytree?style=flat-square)
- [pyfixest](https://github.com/py-econometrics/pyfixest) - Fast high-dimensional fixed-effects regression in Python with IV, Poisson, and modern difference-in-differences estimators. ![GitHub stars](https://img.shields.io/github/stars/py-econometrics/pyfixest?style=flat-square)
- [xtdml](https://github.com/POLSEAN/xtdml) - Stata module for double machine learning in static panel models with fixed effects. ![GitHub stars](https://img.shields.io/github/stars/POLSEAN/xtdml?style=flat-square)

### Difference-in-Differences and Synthetic Control

- [CImpact](https://github.com/Sanofi-Public/CImpact) - Causal impact for time series with frequentist and Bayesian methods. ![GitHub stars](https://img.shields.io/github/stars/Sanofi-Public/CImpact?style=flat-square)
- [contdid](https://github.com/bcallaway11/contdid) - DiD with continuous treatment, by Brantly Callaway. ![GitHub stars](https://img.shields.io/github/stars/bcallaway11/contdid?style=flat-square)
- [diff-diff](https://github.com/igerber/diff-diff) - Python DiD library with Callaway-Sant'Anna, imputation, synthetic DiD, continuous treatment, and Honest DiD, benchmarked against R. ![GitHub stars](https://img.shields.io/github/stars/igerber/diff-diff?style=flat-square)
- [differences](https://github.com/bernardodionisi/differences) - Python implementation of Callaway and Sant'Anna staggered difference-in-differences with multiple periods and triple differences. ![GitHub stars](https://img.shields.io/github/stars/bernardodionisi/differences?style=flat-square)
- [mlsynth](https://github.com/jgreathouse9/mlsynth) - Python library bundling dozens of synthetic control estimators under one API, cross-checked against original implementations. ![GitHub stars](https://img.shields.io/github/stars/jgreathouse9/mlsynth?style=flat-square)
- [moderndid](https://github.com/jordandeklerk/moderndid) - Modern DiD estimators (staggered, continuous, triple, Honest DiD) under one API, scaling to GPUs and Spark or Dask clusters. ![GitHub stars](https://img.shields.io/github/stars/jordandeklerk/moderndid?style=flat-square)
- [pysyncon](https://github.com/sdfordham/pysyncon) - Python synthetic control suite with classic, augmented, penalized, and robust estimators plus placebo inference. ![GitHub stars](https://img.shields.io/github/stars/sdfordham/pysyncon?style=flat-square)
- [scpi](https://nppackages.github.io/scpi/) - Synthetic control with prediction intervals for single, multiple, and staggered-adoption units, in R, Python, and Stata. ![GitHub stars](https://img.shields.io/github/stars/nppackages/scpi?style=flat-square)

### Inference with AI-Generated Data

_Valid estimates and standard errors when regression variables come from LLM or ML predictions._

- [dsl](https://naokiegami.com/dsl/) - Egami, Hinck, Stewart, and Wei's R package for valid regression inference using LLM-annotated variables plus a small expert-coded sample. ![GitHub stars](https://img.shields.io/github/stars/naoki-egami/dsl?style=flat-square)
- [ppi_py](https://github.com/aangelopoulos/ppi_py) - Prediction-powered inference (Science 2023): valid confidence intervals combining a small labeled sample with many ML or LLM predictions. ![GitHub stars](https://img.shields.io/github/stars/aangelopoulos/ppi_py?style=flat-square)
- [ValidMLInference](https://github.com/timothymchristensen/ValidMLInference) - Python package for bias-corrected inference with AI/ML-generated covariates (Battaglia, Christensen, Hansen, Sacher); the R port is MLBC on CRAN. ![GitHub stars](https://img.shields.io/github/stars/timothymchristensen/ValidMLInference?style=flat-square)

### LLM and Foundation-Model Causal Tools

- [Causal AI Scientist](https://github.com/causalNLP/causal-agent) - LLM agent that answers causal questions by choosing and running DiD, IV, RDD, or adjustment estimators, with assumption checks. ![GitHub stars](https://img.shields.io/github/stars/causalNLP/causal-agent?style=flat-square)
- [Causal-Copilot](https://github.com/Lancelot39/Causal-Copilot) - LLM agent automating end-to-end causal discovery, inference, and reporting from natural-language queries. ![GitHub stars](https://img.shields.io/github/stars/Lancelot39/Causal-Copilot?style=flat-square)
- [CausalFM](https://github.com/yccm/CausalFM) - Foundation models for causal inference; pre-trained models replace per-problem estimation (ICLR 2026). ![GitHub stars](https://img.shields.io/github/stars/yccm/CausalFM?style=flat-square)
- [CausalPFN](https://github.com/vdblm/CausalPFN) - Prior-fitted transformer for amortized, in-context ATE and CATE estimation without per-dataset retraining. ![GitHub stars](https://img.shields.io/github/stars/vdblm/CausalPFN?style=flat-square)

## Simulation, Forecasting and Macro Modeling

### Agent-Based Models and LLM Simulation

- [AgentSociety](https://github.com/tsinghua-fib-lab/AgentSociety) - Tsinghua's LLM-agent platform for social-science experiments (AgentSociety 2, 2026), plus the legacy city simulator with economic modules. ![GitHub stars](https://img.shields.io/github/stars/tsinghua-fib-lab/AgentSociety?style=flat-square)
- [BeforeIT.jl](https://github.com/bancaditalia/BeforeIT.jl) - Bank of Italy's agent-based macroeconomic model in Julia. ![GitHub stars](https://img.shields.io/github/stars/bancaditalia/BeforeIT.jl?style=flat-square)
- [Concordia](https://github.com/google-deepmind/concordia) - Google DeepMind library for generative agent-based modeling of social, economic, and market interactions. ![GitHub stars](https://img.shields.io/github/stars/google-deepmind/concordia?style=flat-square)
- [EconAgent](https://github.com/tsinghua-fib-lab/ACL24-EconAgent) - LLM agents with personality traits simulating macroeconomic activities (ACL 2024). ![GitHub stars](https://img.shields.io/github/stars/tsinghua-fib-lab/ACL24-EconAgent?style=flat-square)
- [LLM-ABM Survey](https://github.com/tsinghua-fib-lab/LLM-Agent-Based-Modeling-and-Simulation) - Tsinghua's paper list accompanying its LLM agent-based modeling survey (Humanities and Social Sciences Communications, 2024). ![GitHub stars](https://img.shields.io/github/stars/tsinghua-fib-lab/LLM-Agent-Based-Modeling-and-Simulation?style=flat-square)
- [LLM-Economist](https://github.com/sethkarten/LLM-Economist) - Mechanism design with 3–1,000+ LLM agents for optimal taxation research. ![GitHub stars](https://img.shields.io/github/stars/sethkarten/LLM-Economist?style=flat-square)
- [Magentic Marketplace](https://github.com/microsoft/multi-agent-marketplace) - Microsoft Research environment simulating two-sided markets of LLM buyer and seller agents to study welfare and manipulation. ![GitHub stars](https://img.shields.io/github/stars/microsoft/multi-agent-marketplace?style=flat-square)
- [MarS](https://github.com/microsoft/MarS) - Microsoft engine simulating financial markets via a generative Large Market Model of order flow. ![GitHub stars](https://img.shields.io/github/stars/microsoft/MarS?style=flat-square)
- [Mesa](https://github.com/mesa/mesa) - Python agent-based modeling framework; its Mesa-LLM extension adds language-model decision-making to agents. ![GitHub stars](https://img.shields.io/github/stars/mesa/mesa?style=flat-square)

### Forecasting and Nowcasting

- [Chronos](https://github.com/amazon-science/chronos-forecasting) - Amazon's pretrained forecasting models; Chronos-2 adds zero-shot multivariate and covariate-informed forecasting. ![GitHub stars](https://img.shields.io/github/stars/amazon-science/chronos-forecasting?style=flat-square)
- [Durbyn.jl](https://github.com/taf-society/Durbyn.jl) - Julia port of R's forecast package. ![GitHub stars](https://img.shields.io/github/stars/taf-society/Durbyn.jl?style=flat-square)
- [Moirai (uni2ts)](https://github.com/SalesforceAIResearch/uni2ts) - Salesforce's library for Moirai time-series foundation models (latest Moirai 2.0), with pre-training, fine-tuning, and evaluation code. ![GitHub stars](https://img.shields.io/github/stars/SalesforceAIResearch/uni2ts?style=flat-square)
- [neuralforecast](https://github.com/Nixtla/neuralforecast) - Neural forecasting models (N-BEATS, NHITS, Transformers) for economic time series. ![GitHub stars](https://img.shields.io/github/stars/Nixtla/neuralforecast?style=flat-square)
- [Project Spectrum](https://www.bis.org/project/spectrum) - BIS/ECB/Bundesbank project using GenAI embeddings to classify 34M products for inflation nowcasting (2026 report).
- [statsforecast](https://github.com/Nixtla/statsforecast) - Fast statistical forecasting for econometric time series. ![GitHub stars](https://img.shields.io/github/stars/Nixtla/statsforecast?style=flat-square)
- [Sundial](https://github.com/thuml/Sundial) - Generative time-series foundation models giving probabilistic forecasts via flow matching without discrete tokenization. ![GitHub stars](https://img.shields.io/github/stars/thuml/Sundial?style=flat-square)
- [tabpfn-time-series](https://github.com/PriorLabs/tabpfn-time-series) - Zero-shot time-series forecasting that repurposes the TabPFN-v2 tabular foundation model, no training needed. ![GitHub stars](https://img.shields.io/github/stars/PriorLabs/tabpfn-time-series?style=flat-square)
- [TimeGPT](https://github.com/Nixtla/nixtla) - Nixtla's closed-source, API-based time-series foundation model with a free trial; TimeGPT-2.1 adds multivariate forecasting. ![GitHub stars](https://img.shields.io/github/stars/Nixtla/nixtla?style=flat-square)
- [TimesFM](https://github.com/google-research/timesfm) - Google's time-series foundation model; TimesFM 3.0 (2026) adds zero-shot multivariate forecasting with covariates (self-hosted weights are non-commercial). ![GitHub stars](https://img.shields.io/github/stars/google-research/timesfm?style=flat-square)
- [TiRex-2](https://github.com/NX-AI/tirex-2) - NX-AI's zero-shot forecaster extending TiRex to multivariate series with past and future-known covariates (NeurIPS 2026, Apache-2.0). ![GitHub stars](https://img.shields.io/github/stars/NX-AI/tirex-2?style=flat-square)
- [Toto](https://github.com/DataDog/toto) - Datadog's Apache-2.0 time-series foundation models; Toto 2.0 (2026) spans 4M to 2.5B parameters. ![GitHub stars](https://img.shields.io/github/stars/DataDog/toto?style=flat-square)

### Game Theory and Mechanism Design

- [Axelrod](https://github.com/Axelrod-Python/Axelrod) - Iterated Prisoner's Dilemma research with 200+ strategies and tournament simulations. ![GitHub stars](https://img.shields.io/github/stars/Axelrod-Python/Axelrod?style=flat-square)
- [Nashpy](https://nashpy.readthedocs.io/) - Two-player game solver with support enumeration, vertex enumeration, and Lemke-Howson. ![GitHub stars](https://img.shields.io/github/stars/drvinceknight/Nashpy?style=flat-square)
- [OpenSpiel](https://github.com/google-deepmind/open_spiel) - Google DeepMind library of games with equilibrium-finding and multi-agent learning algorithms such as CFR and PSRO. ![GitHub stars](https://img.shields.io/github/stars/google-deepmind/open_spiel?style=flat-square)
- [pygambit](https://www.gambit-project.org/) - Game theory computation for extensive and strategic form games with a Python API. ![GitHub stars](https://img.shields.io/github/stars/gambitproject/gambit?style=flat-square)

### DSGE and Structural Models

- [Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance](https://github.com/sischei/Deep_Learning_for_Solving_And_Estimating_Dynamic_Economic_Models) - Simon Scheidegger's (Lausanne) open course with runnable notebooks applying deep equilibrium nets and PINNs to DSGE, OLG, and heterogeneous-agent models. ![GitHub stars](https://img.shields.io/github/stars/sischei/Deep_Learning_for_Solving_And_Estimating_Dynamic_Economic_Models?style=flat-square)
- [econpizza](https://github.com/gboehl/econpizza) - JAX-based solver for fully nonlinear heterogeneous-agent (HANK) macroeconomic models via automatic differentiation. ![GitHub stars](https://img.shields.io/github/stars/gboehl/econpizza?style=flat-square)
- [gEconpy](https://github.com/jessegrabowski/gEconpy) - DSGE toolkit in Python. ![GitHub stars](https://img.shields.io/github/stars/jessegrabowski/gEconpy?style=flat-square)
- [MacroModelling.jl](https://github.com/thorek1/MacroModelling.jl) - Julia DSGE toolkit. ![GitHub stars](https://img.shields.io/github/stars/thorek1/MacroModelling.jl?style=flat-square)
- [OpenSourceEconomics](https://github.com/OpenSourceEconomics) - JAX-compatible DC-EGM, Kalman filters, and econ-project-templates.
- [optimagic](https://github.com/optimagic-dev/optimagic) - Numerical optimization for economists (formerly estimagic). ![GitHub stars](https://img.shields.io/github/stars/optimagic-dev/optimagic?style=flat-square)
- [Structural Reinforcement Learning](https://github.com/StructuralRL/SRL) - JAX tutorials by Yang, Wang, Schaab, and Moll solving heterogeneous-agent models with aggregate risk via policy gradients. ![GitHub stars](https://img.shields.io/github/stars/StructuralRL/SRL?style=flat-square)

## Literature Review and Research Discovery

- [alphaXiv](https://www.alphaxiv.org/) - Line-by-line discussion on arXiv papers with AI-powered analysis.
- [ASReview](https://github.com/asreview/asreview) - Active learning for systematic reviews, reducing screening time by up to 95% (Nature Machine Intelligence). ![GitHub stars](https://img.shields.io/github/stars/asreview/asreview?style=flat-square)
- [Asta](https://asta.allen.ai/) - Ai2's agentic-science assistant for paper finding, cited literature reports, and data analysis; successor to the OpenScholar demo. ![GitHub stars](https://img.shields.io/github/stars/allenai/ai2-scholarqa-lib?style=flat-square)
- [Connected Papers](https://www.connectedpapers.com/) - Visual graphs of related papers from a seed paper.
- [Consensus](https://consensus.app/) - AI academic search with quote-linked citations, a multi-step research agent, and API and MCP access.
- [Elicit](https://elicit.com/) - Research agent and PRISMA 2020-aligned systematic reviews over 138M papers, with data extraction and an API and MCP server.
- [Google Scholar Labs](https://scholar.google.com/scholar_labs/search) - Free AI mode in Google Scholar that breaks down research questions and explains how each paper addresses them; sign-in required.
- [Inciteful](https://incitefulmed.com/academic/) - Free citation network analysis using graph algorithms to find key papers and connections.
- [Litmaps](https://www.litmaps.com/) - Dynamic multi-seed citation mapping with monitored searches and daily alerts for new papers.
- [Meta-Mar](https://www.meta-mar.com/) - Free meta-analysis platform where AI reads PDFs and extracts quantitative outcomes.
- [MindMap AI](https://mindmapai.app/) - Turns research papers, PDFs, and notes into structured visual mind maps for literature synthesis.
- [OpenAlex](https://openalex.org/) - Fully open catalog of scholarly works with a free REST API and semantic search.
- [PaperQA2](https://github.com/Future-House/paper-qa) - RAG system for question answering and summarization over scientific literature. ![GitHub stars](https://img.shields.io/github/stars/Future-House/paper-qa?style=flat-square)
- [Rayyan](https://www.rayyan.ai/) - AI-assisted screening and data extraction for systematic reviews, with team collaboration, PRISMA flow diagrams, and a free basic tier.
- [ResearchRabbit](https://www.researchrabbit.ai/) - Citation network and semantic similarity discovery rebuilt with Litmaps.
- [SciSpace](https://scispace.com/) - Deep review with iterative search and Zotero integration across 280M papers.
- [Scite](https://scite.ai/) - Smart Citations classifying 1.6B+ citations as supporting or contrasting, plus an AI assistant, Reference Check, and MCP access.
- [Semantic Scholar](https://www.semanticscholar.org/) - AI-powered academic search with citation analysis, TLDR summaries, and free API across 220M+ papers.
- [Suppr](https://suppr.ai/) - AI literature search, document translation, and deep-research reports over PubMed and OpenAlex, with a Zotero plugin.
- [Undermind](https://www.undermind.ai/) - Autonomously reads hundreds of papers and produces structured reports with timelines and categories.
- [Zotero MCP](https://github.com/54yyyu/zotero-mcp) - Connects your Zotero library to Claude, ChatGPT, Codex, and Cursor to search, read, annotate, and cite papers. ![GitHub stars](https://img.shields.io/github/stars/54yyyu/zotero-mcp?style=flat-square)
- [Zotero PapersGPT](https://github.com/papersgpt/papersgpt-for-zotero) - Zotero AI plugin supporting ChatGPT, Claude, Gemini, and more for PDF chat and summaries. ![GitHub stars](https://img.shields.io/github/stars/papersgpt/papersgpt-for-zotero?style=flat-square)

## Economic Data and Analysis

### AI Data Analysis Platforms

- [Julius AI](https://julius.ai/) - Upload datasets and ask questions in natural language; returns charts, regressions, and reports.
- [Microsoft Data Formulator](https://github.com/microsoft/data-formulator) - Describe charts in English and get publication-quality output with Python code. ![GitHub stars](https://img.shields.io/github/stars/microsoft/data-formulator?style=flat-square)

### Economic Data Sources

- [FRED API v2](https://fred.stlouisfed.org/docs/api/fred/) - Bulk retrieval of all series in any release across 800,000+ time series.
- [FXMacroData](https://fxmacrodata.com/) - API and MCP server for macroeconomic releases, calendars, FX, commodities, and bond yields, queryable in plain English.
- [Global Macro Database](https://www.globalmacrodata.com/) - Macroeconomic dataset, free for academic use, covering 239 countries from 1086 to 2025 with forecasts to 2031, plus MCP access. ![GitHub stars](https://img.shields.io/github/stars/KMueller-Lab/Global-Macro-Database?style=flat-square)
- [UN System Data Commons](https://data.un.org/) - Official UN statistics portal (successor to UNdata) built on Data Commons, with natural-language search and MCP access.

## Academic Writing and LaTeX

_Agent skills for paper writing, refereeing, and slides are listed under Agent Skills for Economists above._

- [bibverify](https://github.com/Hylouis233/bibverify) - Verifies BibTeX entries against Crossref, OpenAlex, Semantic Scholar, and arXiv via CLI, MCP server, or agent skill. ![GitHub stars](https://img.shields.io/github/stars/Hylouis233/bibverify?style=flat-square)
- [OpenAI Prism](https://openai.com/prism/) - Free LaTeX workspace with citation management, Zotero sync, sketch-to-equation, and real-time collaboration.
- [Overleaf AI](https://www.overleaf.com/about/ai-features) - LaTeX error fixing, table and equation generation, and writing feedback, included in all Overleaf plans with a basic free allowance.
- [**overleaf-sync-now**](https://github.com/hanlulong/overleaf-sync-now) - Agent skill and CLI that pull recent Overleaf web edits into a Dropbox-synced copy before AI agents edit it. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/overleaf-sync-now?style=flat-square)
- [Paperpal](https://paperpal.com/) - Academic writing assistant on Overleaf, Google Docs, and Chrome.
- [Refine.ink](https://www.refine.ink/) - AI technical verification flagging errors in reasoning, calculations, and references; used by AEA and Econometric Society journals.
- [Thesify](https://www.thesify.ai/) - AI reviewer evaluating argumentation, methodology, and rigor.
- [Typst](https://typst.app/) - Markup-based typesetting system and LaTeX alternative with simpler syntax, incremental compilation, and a collaborative web editor. ![GitHub stars](https://img.shields.io/github/stars/typst/typst?style=flat-square)
- [Underleaf](https://www.underleaf.ai/) - Chrome extension for image-to-LaTeX and smart citation generation.

## Document Processing and OCR

- [Chandra](https://github.com/datalab-to/chandra) - Datalab's open-weight OCR model converting images and PDFs to Markdown or JSON, handling handwriting, forms, and complex tables. ![GitHub stars](https://img.shields.io/github/stars/datalab-to/chandra?style=flat-square)
- [CHURRO](https://github.com/stanford-oval/Churro) - Stanford's open-weight OCR model for handwritten and printed historical documents across 46 language clusters (EMNLP 2025). ![GitHub stars](https://img.shields.io/github/stars/stanford-oval/Churro?style=flat-square)
- [DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR) - Open-weight vision model converting document images to Markdown with formula and table recognition, succeeded by [DeepSeek-OCR 2](https://github.com/deepseek-ai/DeepSeek-OCR-2) in 2026. ![GitHub stars](https://img.shields.io/github/stars/deepseek-ai/DeepSeek-OCR?style=flat-square)
- [Docling](https://github.com/docling-project/docling) - Open-source parser, created at IBM, converting PDFs, Office files, scans, and XBRL financial reports into Markdown or JSON. ![GitHub stars](https://img.shields.io/github/stars/docling-project/docling?style=flat-square)
- [eScriptorium](https://gitlab.com/scripta/escriptorium) - Open-source platform for segmenting, transcribing, and OCR-ing historical and handwritten manuscripts.
- [Marker](https://github.com/datalab-to/marker) - Converts PDFs, Office files, and images to Markdown or JSON with tables, equations, and forms; LLM mode merges cross-page tables. ![GitHub stars](https://img.shields.io/github/stars/datalab-to/marker?style=flat-square)
- [Mathpix](https://mathpix.com/) - Screenshot-to-LaTeX OCR for equations, tables, and diagrams with PDF-to-Overleaf conversion.
- [MinerU](https://github.com/opendatalab/MinerU) - Converts PDFs, scans, Office files, and e-books into LLM-ready Markdown or JSON with tiered local parsing (v4, 2026). ![GitHub stars](https://img.shields.io/github/stars/opendatalab/MinerU?style=flat-square)
- [Mistral OCR](https://mistral.ai/news/ocr-4/) - Pay-per-page document OCR API returning text with bounding boxes, block types, and confidence scores in 170 languages.
- [olmOCR](https://github.com/allenai/olmocr) - Ai2's fully open OCR toolkit and model (olmOCR 2) for tables, equations, and handwriting, plus the olmOCR-Bench benchmark. ![GitHub stars](https://img.shields.io/github/stars/allenai/olmocr?style=flat-square)
- [PaddleOCR-VL](https://github.com/PaddlePaddle/PaddleOCR) - Compact 0.9B vision-language OCR (v1.6, 2026) extracting layout, formulas, tables, and charts, including from historical documents. ![GitHub stars](https://img.shields.io/github/stars/PaddlePaddle/PaddleOCR?style=flat-square)
- [Pix2Text](https://github.com/breezedeus/Pix2Text) - Open-source tool recognizing layouts, tables, and math formulas in images, exporting LaTeX and Markdown. ![GitHub stars](https://img.shields.io/github/stars/breezedeus/Pix2Text?style=flat-square)
- [Surya](https://github.com/datalab-to/surya) - Open-source OCR toolkit for 90+ languages with layout, reading-order, and table recognition. ![GitHub stars](https://img.shields.io/github/stars/datalab-to/surya?style=flat-square)
- [Transkribus](https://www.transkribus.org/) - Cooperative-run platform transcribing handwritten and printed historical documents with 300+ community AI models; 50 free credits monthly.

## NLP and Text as Data

- [CentralBankRoBERTa](https://github.com/Moritz-Pfeifer/CentralBankRoBERTa) - Fine-tuned RoBERTa for sentiment classification in central bank communications. ![GitHub stars](https://img.shields.io/github/stars/Moritz-Pfeifer/CentralBankRoBERTa?style=flat-square)
- [ChronoGPT](https://huggingface.co/manelalab) - Open language models with yearly checkpoints (1999–2024), each trained only on text available through that year to avoid lookahead bias.
- [EconBERTa](https://github.com/worldbank/econberta-econie) - World Bank DeBERTa trained on 9.4B tokens from 1.5M economics papers with NER. ![GitHub stars](https://img.shields.io/github/stars/worldbank/econberta-econie?style=flat-square)
- [FinBERT](https://huggingface.co/ProsusAI/finbert) - Fine-tuned BERT for financial sentiment, widely cited in economics and finance research.
- [GABRIEL](https://github.com/openai/GABRIEL) - OpenAI toolkit turning text, images, or audio into quantitative measures for social scientists. ![GitHub stars](https://img.shields.io/github/stars/openai/GABRIEL?style=flat-square)
- [LinkTransformer](https://github.com/dell-research-harvard/linktransformer) - Arora and Dell's (Harvard) Python package for transformer-based record linkage, deduplication, and classification of messy text in dataframes. ![GitHub stars](https://img.shields.io/github/stars/dell-research-harvard/linktransformer?style=flat-square)
- [OccCANINE](https://github.com/christianvedels/OccCANINE) - Model converting free-text occupational descriptions in 13 languages into HISCO codes with about 96% accuracy. ![GitHub stars](https://img.shields.io/github/stars/christianvedels/OccCANINE?style=flat-square)
- [WorldCentralBanks](https://github.com/gtfintechlab/WorldCentralBanks) - Annotated corpus and per-bank models classifying monetary policy stance in central bank communications worldwide. ![GitHub stars](https://img.shields.io/github/stars/gtfintechlab/WorldCentralBanks?style=flat-square)

## Policy, Labor and Alternative Data

### Policy and Evidence Synthesis

- [EUROMOD](https://euromod-web.jrc.ec.europa.eu/) - EU tax-benefit microsimulation covering all 27 member states (open-source, EUPL-1.2).
- [ImpactAI](https://impactai.worldbank.org/) - World Bank DIME tool synthesizing RCT evidence with effect sizes across interventions.
- [OpenFisca](https://openfisca.org/en/) - Open-source microsimulation engine for computing taxes and benefits on population data. ![GitHub stars](https://img.shields.io/github/stars/openfisca/openfisca-core?style=flat-square)
- [PolicyEngine](https://www.policyengine.org/) - Open-source tax-benefit microsimulation for the U.S., UK, and Canada with a free web app, API, and Claude Code plugin. ![GitHub stars](https://img.shields.io/github/stars/PolicyEngine/policyengine-us?style=flat-square)

### Labor Market Data

- [Lightcast](https://lightcast.io/) - Global job-postings and skills data across 165 countries, plus the free Open Skills taxonomy of 34,000+ skills.
- [LinkedIn Economic Graph](https://economicgraph.linkedin.com/) - Research and interactive data on hiring, skills, and AI's effect on work, including the monthly LinkedIn Workforce Report.
- [Revelio Labs](https://www.reveliolabs.com/) - Workforce data with free monthly RPLS U.S. labor statistics, a monthly AI Labor Market Tracker, and academic access via WRDS.

### AI Adoption and Exposure Trackers

- [AI Economic Indicators](https://digitaleconomy.stanford.edu/project/indicators/) - Stanford Digital Economy Lab's monthly dashboards on AI's effects on employment, adoption, and consumer surplus.
- [Anthropic Economic Index](https://www.anthropic.com/economic-index) - CC BY dataset and recurring reports on Claude use by O*NET task, occupation, and region, queryable through a Claude connector.
- [Census BTOS](https://www.census.gov/programs-surveys/btos.html) - Census Bureau's biweekly business survey tracking current and expected AI use by sector, state, and firm size.
- [GenAI Adoption Tracker](https://www.genaiadoptiontracker.com/) - Bick, Blandin, and Deming's nationally representative survey of U.S. generative AI use at work and home.
- [GPTs are GPTs](https://github.com/openai/GPTs-are-GPTs) - Task- and occupation-level LLM exposure scores for O*NET from Eloundou et al. (Science, 2024). ![GitHub stars](https://img.shields.io/github/stars/openai/GPTs-are-GPTs?style=flat-square)
- [Indeed Hiring Lab AI Tracker](https://github.com/hiring-lab/ai-tracker) - Daily share of Indeed job postings mentioning AI in nine countries since 2019, under CC BY 4.0. ![GitHub stars](https://img.shields.io/github/stars/hiring-lab/ai-tracker?style=flat-square)
- [Microsoft Global AI Diffusion Report](https://www.microsoft.com/en-us/corporate-responsibility/topics/ai-economy-institute/reports/global-ai-diffusion-report/) - Quarterly telemetry-based estimates of generative AI use among working-age adults in 147 economies.
- [OpenAI Signals](https://openai.com/signals/) - OpenAI's economic research hub with quarterly downloadable data on ChatGPT adoption and use by country, age, and task.
- [Ramp AI Index](https://ramp.com/data/ai-index) - Monthly share of U.S. businesses on Ramp paying for AI tools, by industry, size, and provider; also on FRED.
- [Yale Budget Lab AI Tracker](https://budgetlab.yale.edu/research/tracking-impact-ai-labor-market) - Regularly updated CPS-based analysis, with data, of whether AI is shifting U.S. occupations and unemployment.

### Spatial, Satellite and Alternative Data

- [AlphaEarth Satellite Embeddings](https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_SATELLITE_EMBEDDING_V1_ANNUAL) - Google DeepMind's annual global 10-meter, 64-dimension satellite embeddings since 2017 on Earth Engine.
- [Clay Foundation Model](https://madewithclay.org) - Open foundation model for Earth observation generating embeddings from global multi-sensor satellite imagery. ![GitHub stars](https://img.shields.io/github/stars/Clay-foundation/model?style=flat-square)
- [MOSAIKS](https://www.mosaiks.org/) - Precomputed satellite-imagery features and API for predicting local socioeconomic outcomes, including HDI for 61,530 municipalities (Nature Communications, 2026).
- [Overture Maps](https://overturemaps.org) - Open global geospatial data of places, buildings, addresses, and transportation, released monthly. ![GitHub stars](https://img.shields.io/github/stars/OvertureMaps/data?style=flat-square)

## Finance-Specific AI

- [ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) - Educational multi-agent system mimicking famous investors to research stocks and propose trading decisions. ![GitHub stars](https://img.shields.io/github/stars/virattt/ai-hedge-fund?style=flat-square)
- [awesome-quant](https://github.com/wilsonfreitas/awesome-quant) - Curated quantitative finance resources. ![GitHub stars](https://img.shields.io/github/stars/wilsonfreitas/awesome-quant?style=flat-square)
- [Dexter](https://github.com/virattt/dexter) - Autonomous financial research agent with task planning and real-time data. ![GitHub stars](https://img.shields.io/github/stars/virattt/dexter?style=flat-square)
- [EdgarTools](https://github.com/dgunning/edgartools) - Python library turning SEC EDGAR filings and XBRL financials into DataFrames and LLM-ready text, with a built-in MCP server. ![GitHub stars](https://img.shields.io/github/stars/dgunning/edgartools?style=flat-square)
- [Fin-R1](https://github.com/SUFE-AIFLM-Lab/Fin-R1) - Financial reasoning LLM by Shanghai University of Finance and Economics. ![GitHub stars](https://img.shields.io/github/stars/SUFE-AIFLM-Lab/Fin-R1?style=flat-square)
- [FinGPT](https://github.com/AI4Finance-Foundation/FinGPT) - Open-source financial LLMs for sentiment, forecasting, and reports. ![GitHub stars](https://img.shields.io/github/stars/AI4Finance-Foundation/FinGPT?style=flat-square)
- [FinRobot](https://github.com/AI4Finance-Foundation/FinRobot) - AI agent platform for financial analysis combining LLMs, RL, and quantitative methods. ![GitHub stars](https://img.shields.io/github/stars/AI4Finance-Foundation/FinRobot?style=flat-square)
- [OpenBB](https://github.com/openbq-org/OpenBB) - Open-source data platform connecting financial and economic data to Python and AI agents via MCP, stewarded by the non-profit OpenBQ. ![GitHub stars](https://img.shields.io/github/stars/openbq-org/OpenBB?style=flat-square)
- [TradingAgents](https://github.com/TauricResearch/TradingAgents) - Multi-agent LLM framework simulating analyst, researcher, trader, and risk-manager roles for trading decisions. ![GitHub stars](https://img.shields.io/github/stars/TauricResearch/TradingAgents?style=flat-square)

## Data Collection Tools

### Web Scraping

- [Crawl4AI](https://github.com/unclecode/crawl4ai) - Open-source web crawler producing LLM-ready markdown for RAG and data pipelines. ![GitHub stars](https://img.shields.io/github/stars/unclecode/crawl4ai?style=flat-square)
- [Crawlee](https://crawlee.dev) - Open-source crawling and scraping library that extracts web data for AI, LLM, and RAG pipelines. ![GitHub stars](https://img.shields.io/github/stars/apify/crawlee?style=flat-square)
- [Firecrawl](https://www.firecrawl.dev/) - Open-source API turning websites into LLM-ready Markdown or structured JSON, with an AI agent for schema-based extraction. ![GitHub stars](https://img.shields.io/github/stars/firecrawl/firecrawl?style=flat-square)
- [ScrapeGraphAI](https://github.com/ScrapeGraphAI/Scrapegraph-ai) - LLM-powered scraping that adapts to website changes automatically. ![GitHub stars](https://img.shields.io/github/stars/ScrapeGraphAI/Scrapegraph-ai?style=flat-square)

### Survey and Qualitative Research

- [ATLAS.ti](https://atlasti.com/) - Qualitative data analysis software with AI coding, document chat, and transcription, plus a free trial and student licenses.
- [Conversations at Scale](https://github.com/friedrichgeiecke/interviews) - Geiecke and Jaravel's (LSE) platform for AI-led qualitative interviews, free for non-commercial research. ![GitHub stars](https://img.shields.io/github/stars/friedrichgeiecke/interviews?style=flat-square)
- [EDSL](https://github.com/expectedparrot/edsl) - Open-source Python library from Expected Parrot (co-founded by economist John Horton) for surveys and experiments with LLM agents. ![GitHub stars](https://img.shields.io/github/stars/expectedparrot/edsl?style=flat-square)
- [QualCoder](https://github.com/ccbogel/QualCoder) - Open-source qualitative coding app for text, images, audio, and video, with an AI agent that searches data and proposes codes. ![GitHub stars](https://img.shields.io/github/stars/ccbogel/QualCoder?style=flat-square)
- [Twin-2K-500](https://huggingface.co/datasets/LLM-Digital-Twin/Twin-2K-500) - Columbia dataset of 2,058 U.S. respondents answering about 500 survey and behavioral-economics questions, for testing LLM digital twins.

> **Warning:** [Nature](https://www.nature.com/articles/d41586-026-00221-8) reports AI chatbots infiltrating online surveys. Implement detection for MTurk/Prolific studies.

### Synthetic Data

- [MOSTLY AI](https://github.com/mostly-ai/mostlyai) - Open-source SDK generating synthetic tabular, multi-table, and time-series data locally, with optional differential privacy. ![GitHub stars](https://img.shields.io/github/stars/mostly-ai/mostlyai?style=flat-square)
- [REaLTabFormer](https://github.com/worldbank/REaLTabFormer) - World Bank library using transformers to generate synthetic single-table and relational data. ![GitHub stars](https://img.shields.io/github/stars/worldbank/REaLTabFormer?style=flat-square)
- [SDV](https://github.com/sdv-dev/SDV) - Open-source synthetic data generation with CTGAN, CopulaGAN, and GaussianCopula models. ![GitHub stars](https://img.shields.io/github/stars/sdv-dev/SDV?style=flat-square)
- [Synthcity](https://github.com/vanderschaarlab/synthcity) - Generates and benchmarks synthetic tabular, time-series, and survival data with privacy and fairness metrics. ![GitHub stars](https://img.shields.io/github/stars/vanderschaarlab/synthcity?style=flat-square)

## Benchmarks and Evaluation

_Benchmarks and leaderboards for judging how well AI handles economic reasoning, forecasting, finance, replication, and real work tasks._

- [ForecastBench](https://www.forecastbench.org/) - Forecasting Research Institute's live benchmark of LLM vs. superforecaster accuracy, including FRED-based questions (ICLR 2025). ![GitHub stars](https://img.shields.io/github/stars/forecastingresearch/forecastbench?style=flat-square)
- [GDPval](https://huggingface.co/datasets/openai/gdpval) - OpenAI benchmark of real work tasks in 44 occupations from the top nine U.S. GDP sectors, with 220 tasks open-sourced.
- [Open Financial LLM Leaderboard](https://huggingface.co/spaces/TheFinAI/Open-FinLLM-Leaderboard) - Public leaderboard benchmarking LLMs across financial NLP, question answering, and forecasting tasks.
- [Remote Labor Index](https://labs.scale.com/leaderboard/rli) - Scale AI and CAIS benchmark of 240 real freelance projects, measuring the share AI agents complete at professional quality.
- [REPRO-Bench](https://github.com/uiuc-kang-lab/REPRO-Bench) - Benchmark of 112 social-science papers, mainly economics and political science, testing whether AI agents can assess reproducibility (ACL Findings 2025). ![GitHub stars](https://img.shields.io/github/stars/uiuc-kang-lab/REPRO-Bench?style=flat-square)
- [STEER](https://steer-benchmark.cs.ubc.ca/) - UBC benchmarks of LLM economic rationality and microeconomic reasoning (ICML 2024, NeurIPS 2025). ![GitHub stars](https://img.shields.io/github/stars/narunraman/STEER?style=flat-square)

## Papers and Books

### Key Papers

_Grouped by theme, newest first._

#### Using AI in Economic Research

- [AI-Assisted Teams Outperform AI-Led Teams but Not Human-Only Teams in Assessing Research Reproducibility in Quantitative Social Science](https://www.pnas.org/doi/10.1073/pnas.2524747123) - Brodeur et al. (2026), Proceedings of the National Academy of Sciences.
- [Teaching Economics to the Machines](https://www.nber.org/papers/w34713) - Chen et al. (2026), NBER Working Paper 34713.
- [Performing Valid Inference with AI/ML-Generated Covariates: A Guide for Empirical Practice](https://www.aeaweb.org/articles?id=10.1257/pandp.20261020) - Christensen and Hansen (2026), AEA Papers and Proceedings.
- [A Practitioner's Guide to Using Large Language Models and Generative AI in Economic History](https://www.nber.org/papers/w35374) - Ferrara (2026), NBER Working Paper 35374.
- [Large Language Models: An Applied Econometric Framework](https://doi.org/10.1146/annurev-economics-120925-105620) - Ludwig, Mullainathan, and Rambachan (2026), Annual Review of Economics.
- [Machine Learning Who to Nudge: Causal vs Predictive Targeting in a Field Experiment on Student Financial Aid Renewal](https://doi.org/10.1016/j.jeconom.2024.105945) - Athey, Keleher, and Spiess (2025), Journal of Econometrics.
- [Artificial Intelligence in Economics Research: What Have We Learned? What Do We Need to Learn?](https://onlinelibrary.wiley.com/doi/10.1111/joes.12694) - Bahoo et al. (2025), Journal of Economic Surveys.
- [Deep Learning for Economists](https://www.aeaweb.org/articles?id=10.1257/jel.20241733) - Dell (2025), Journal of Economic Literature.
- [Difference-in-Difference Causal Forests with an Application to Payroll Tax Incidence in Norway](https://onlinelibrary.wiley.com/doi/10.1002/jae.70001) - Gavrilova, Langørgen, and Zoutman (2025), Journal of Applied Econometrics.
- [AI Agents for Economic Research](https://www.nber.org/papers/w34202) - Korinek (2025), NBER Working Paper 34202.
- [Economics in the Age of Algorithms](https://www.aeaweb.org/articles?id=10.1257/pandp.20251118) - Mullainathan (2025), AEA Papers and Proceedings.
- [Machine Learning as a Tool for Hypothesis Generation](https://academic.oup.com/qje/article/139/2/751/7515309) - Ludwig and Mullainathan (2024), Quarterly Journal of Economics.
- [Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?](https://www.nber.org/papers/w31122) - Horton, Filippas, and Manning (2023), NBER Working Paper 31122.
- [Generative AI for Economic Research: Use Cases and Implications for Economists](https://www.aeaweb.org/articles?id=10.1257/jel.20231736) - Korinek (2023), Journal of Economic Literature.

#### Economics of AI

- [The Emerging Market for Intelligence: How Firms Buy and Sell AI](https://www.aeaweb.org/articles?id=10.1257/jep.20261506) - Demirer, Fradkin, and Tadelis (2026), Journal of Economic Perspectives.
- [AI and Our Economic Future](https://www.aeaweb.org/articles?id=10.1257/jep.20261505) - Jones (2026), Journal of Economic Perspectives.
- [Economic Scenarios for Transformative AI](https://web.stanford.edu/~chadj/econscenarios.pdf) - Korinek et al. (2026), CEPR Discussion Paper 21939.
- [The Simple Macroeconomics of AI](https://academic.oup.com/economicpolicy/article/40/121/13/7728473) - Acemoglu (2025), Economic Policy.
- [Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence](https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine-six-facts-about-the-recent-employment-effects-of-artificial-intelligence/) - Brynjolfsson, Chandar, and Chen (2025), Stanford Digital Economy Lab working paper.
- [A Research Agenda for the Economics of Transformative AI](https://www.nber.org/papers/w34256) - Brynjolfsson, Korinek, and Agrawal (2025), NBER Working Paper 34256.
- [Generative AI at Work](https://academic.oup.com/qje/article/140/2/889/7990658) - Brynjolfsson, Li, and Raymond (2025), Quarterly Journal of Economics.
- [How People Use ChatGPT](https://www.nber.org/papers/w34255) - Chatterji et al. (2025), NBER Working Paper 34255.

### Books

- [Applied Causal Inference Powered by ML and AI](https://causalml-book.org/) - Free textbook by Chernozhukov, Hansen, Kallus, Spindler, and Syrgkanis on double/debiased ML, with R and Python notebooks.
- [The Economics of Transformative AI](https://www.nber.org/books-and-chapters/economics-transformative-ai) - Agrawal, Brynjolfsson, and Korinek's NBER volume of 16 studies on AI agents, labor, growth, and risk (UChicago Press, 2026).
- [The Means of Prediction](https://press.uchicago.edu/ucp/books/book/chicago/M/bo255887145.html) - Maximilian Kasy on how AI works and who benefits (UChicago Press, 2025).
- [The Scaling Era](https://press.stripe.com/scaling) - Dwarkesh Patel and Gavin Leech's oral history of AI from interviews with Amodei, Hassabis, Zuckerberg, and others (Stripe Press, 2025).

## Courses, Conferences and Community

### Courses, Guides and Tutorials

- [AI for Economic Theorists and Mathematicians](https://markusacademy.substack.com/p/ai-for-economic-theorists-and-mathematicians) - Markus' Academy series by Pietro Ortoleva and Fedor Sandomirskiy (Princeton) on AI for modeling and proofs.
- [AI for Economists](https://policy.fi/ai-econ/) - Jesse Lastunen's curated, filterable directory of papers, courses, tools, and talks on AI in economics.
- [AI Tools for Economists and Policy Analysts](https://www.aei.org/domestic-policy/technology-and-innovation/ai-tools-for-economists-and-policy-analysts/) - Will Rinehart's (AEI) regularly updated guide mapping AI tools and prompts to economics and policy tasks.
- [Claude Blattman](https://claudeblattman.com/) - Chris Blattman's (UChicago) open-source guide to AI research workflows with Claude Code, no coding required, plus an installable skills plugin. ![GitHub stars](https://img.shields.io/github/stars/chrisblattman/claudeblattman?style=flat-square)
- [Claude Code for Applied Economists](https://markusacademy.substack.com/p/claude-code-for-applied-economists) - Paul Goldsmith-Pinkham's (Yale) eight-episode video series on data work, scraping, skills, sandboxing, and Overleaf.
- [Data Analysis with AI](https://gabors-data-analysis.com/ai-course/) - Gábor Békés's (CEU) eight-session open course using AI coding agents for data wrangling, econometrics, text as data, and DiD.
- [EconDL](https://econdl.github.io/) - Melissa Dell's companion site to Deep Learning for Economists, with demo notebooks, software resources, and lectures.
- [Economics of Transformative AI](https://digitaleconomy.stanford.edu/about/education/the-economics-of-transformative-ai/) - Stanford Digital Economy Lab summer course (2025) with open slides, exercises, and recorded lectures.
- [genaiforecon.org](https://www.genaiforecon.org/) - Korinek's companion site to his JEL survey, with periodic updates on LLM tools; the latest (August 2025) covers AI agents.
- [How to Learn and Teach Economics with LLMs](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4391863) - Cowen and Tabarrok's (GMU) practical guide to using GPT for learning, teaching, and researching economics.
- [Machine Learning and Causal Inference](https://www.gsb.stanford.edu/faculty-research/labs-initiatives/sil/research/methods/ai-machine-learning/short-course) - Video course from Susan Athey's Stanford GSB lab on ML for treatment effects, heterogeneous impacts, and targeting, with R tutorials.
- [ML and Economics at Oxford](https://maxkasy.github.io/home/ML_Econ_Oxford/) - Maximilian Kasy's reading group.
- [Modern AI for Economics Research](https://markusacademy.substack.com/p/modern-ai-for-economics-research) - Markus' Academy talk by Benjamin Golub on Cursor, AI refereeing, and prompting for research.
- [NBER Methods Lecture: AI-Generated Data](https://www.nber.org/research/videos/2026-methods-lecture-melissa-dell-and-ashesh-rambachan-estimation-and-inference-ai-generated-data) - Melissa Dell and Ashesh Rambachan's 2026 Summer Institute lectures on estimation and inference with AI-generated data.
- [Reflections on Vibe Researching](https://joshuagans.substack.com/p/reflections-on-vibe-researching) - Joshua Gans (Toronto) on where LLMs aid theory work and where human judgment stays essential.
- [Research in the Time of AI](https://paulgp.substack.com/p/research-in-the-time-of-ai) - Paul Goldsmith-Pinkham (Yale) on where AI compresses the research timeline and where taste matters.
- [The Economics of AI](https://www.coursera.org/learn/economics-of-ai) - Anton Korinek's (UVA) Coursera course on AI's implications for economic growth, labor markets, inequality, and policy.
- [Using AI in Research and Teaching](https://paulgp.com/2024/06/24/llm_talk.html) - Paul Goldsmith-Pinkham's (Yale) 2024 practical guide to Copilot in VS Code, chat LLMs, and local models for research and teaching.

### Conferences

- [ESIF Economics and AI+ML Meeting](https://www.econometricsociety.org/regional-activities/schedule/2026/06/16/2026-ESIFEconomics-and-AIML-Meeting) - Econometric Society's biennial interdisciplinary meeting on economics and AI/ML (latest: Cornell, June 16–17, 2026).
- [NBER Digital Economics and AI Meeting](https://www.nber.org/conferences/digital-economics-and-ai-meeting-spring-2027) - Stanford, January 21–22, 2027; paper submissions and PhD tutorial applications due November 3, 2026.
- [NBER Economics of AI Conference](https://www.nber.org/conferences/economics-artificial-intelligence-fall-2026) - Annual fall conference in Toronto organized by Agrawal, Gans, Goldfarb, and Tucker (latest: September 23–24, 2026).

### Community

**Newsletters:** [Autonomous Econ](https://autonomousecon.substack.com/) (Wong) | [Frankly, the Counterfactual Was Worse](https://franklythecounterfactual.substack.com/) (IU O'Neill) | [genaiforecon](https://genaiforecon.substack.com/) (Korinek) | [One Useful Thing](https://www.oneusefulthing.org/) (Mollick) | [paulgp](https://paulgp.substack.com/) (Goldsmith-Pinkham) | [Scott's Mixtape](https://causalinf.substack.com/) (Cunningham)

**Podcasts:** [Dwarkesh Podcast](https://www.dwarkesh.com/podcast) | [Exponential View](https://podcasts.apple.com/us/podcast/azeem-azhars-exponential-view/id1172218725) | [Justified Posteriors](https://empiricrafting.substack.com/) (Benzell and Fradkin)

**People:** [Erik Brynjolfsson](https://www.brynjolfsson.com/) | [Scott Cunningham](https://www.scunning.com/) | [Melissa Dell](https://dell-research-harvard.github.io/) | [Anton Korinek](https://www.korinek.com/) | [Antonio Mele](https://www.lse.ac.uk/people/antonio-mele) | [Sendhil Mullainathan](https://sendhil.org/)

**Institutions:** [EconTAI](https://www.econtai.org/) | [NBER Digital Economics and AI](https://www.nber.org/digitization) | [OECD.AI](https://oecd.ai/) | [Stanford DEL](https://digitaleconomy.stanford.edu/)

## Appendix: General-Purpose AI

_Widely known tools listed for completeness with notes on what economists specifically value._

- [ChatGPT](https://chatgpt.com/) - Deep Research that can focus on sites you trust, a Work agent for spreadsheets and decks, and an Excel add-in.
- [Claude](https://claude.ai/) - Coding help for Stata, R, and Python, 1M-token context for long documents, Research mode, and Claude for Excel.
- [Claude Code](https://code.claude.com/docs) - Anthropic's agentic coding tool for the terminal, IDE, desktop app, and browser, extensible with MCP servers and agent skills.
- [Cline](https://github.com/cline/cline) - Open-source coding agent for VS Code and the terminal that works with many model providers, including local models. ![GitHub stars](https://img.shields.io/github/stars/cline/cline?style=flat-square)
- [Cursor](https://cursor.com/) - AI code editor with agent mode, parallel Cloud Agents, and a free Hobby tier.
- [DeepSeek](https://huggingface.co/deepseek-ai) - MIT-licensed open-weight models with 1M-token context, plus a low-cost API for large-scale text classification.
- [Gemini](https://gemini.google.com/) - Deep Research reports from hundreds of sites (optionally your Gmail and Drive), with Canvas for drafts and visuals.
- [Gemini Notebook](https://notebook.google.com/) - Formerly NotebookLM: cited Q&A over your papers, Audio and Video Overviews, and code execution for data analysis on paid tiers.
- [GitHub Copilot](https://github.com/features/copilot) - Free and Student plans, agent mode in VS Code, a cloud coding agent, and completions-only support in [RStudio](https://docs.posit.co/ide/user/ide/guide/tools/copilot.html).
- [Ollama](https://ollama.com/) - Free local runner for open-weight models (gpt-oss, Qwen, Gemma, DeepSeek), so confidential microdata never leaves your machine. ![GitHub stars](https://img.shields.io/github/stars/ollama/ollama?style=flat-square)
- [OpenAI Codex](https://openai.com/codex/) - Coding agent in the ChatGPT desktop app, open-source CLI, and IDE, running parallel local and cloud tasks with reusable skills. ![GitHub stars](https://img.shields.io/github/stars/openai/codex?style=flat-square)
- [OpenCode](https://github.com/anomalyco/opencode) - Open-source coding agent for the terminal and desktop that works with 75+ model providers, including local models. ![GitHub stars](https://img.shields.io/github/stars/anomalyco/opencode?style=flat-square)
- [Perplexity](https://www.perplexity.ai/) - Cited answers with an Academic source filter for scholarly papers, plus multi-step Research reports.

## Contributing

Contributions welcome! Read the [contribution guidelines](CONTRIBUTING.md) first.

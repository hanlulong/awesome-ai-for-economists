# Awesome AI for Economists [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![Last Commit](https://img.shields.io/github/last-commit/hanlulong/awesome-ai-for-economists)](https://github.com/hanlulong/awesome-ai-for-economists/commits/main)

A curated list of AI tools, libraries, and resources transforming how economists conduct research, teach, and analyze policy — from natural language data access to causal machine learning.

> **Scope:** Tools with specific value for economists. General-purpose AI assistants are in the [Appendix](#appendix-general-purpose-ai).

### Highlights

> This list is maintained by the [OpenEcon](https://openecon.ai/) team — building open-source infrastructure connecting AI to economics.
>
> - **[AI-research-setup](https://github.com/hanlulong/AI-research-setup)** — New to this? Start here to set up Claude Code and Codex for economics research on macOS and Windows. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/AI-research-setup?style=flat-square)
> - **[OpenEcon Data](https://openecon.ai/)** — Query 330,000+ economic indicators from FRED, World Bank, IMF, and 10+ sources in plain English. Available as [web app](https://data.openecon.ai), Python API, and [MCP server](https://github.com/hanlulong/openecon-data). ![GitHub stars](https://img.shields.io/github/stars/hanlulong/openecon-data?style=flat-square)
> - **[Stata-MCP](https://github.com/hanlulong/stata-mcp)** — Run Stata from VS Code, Cursor, Claude Code, and GitHub Copilot with real-time output, data viewer, and graph display. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/stata-mcp?style=flat-square)
> - **[Econ Writing Skill](https://github.com/hanlulong/econ-writing-skill)** — AI agent skill for writing economics papers, synthesizing 50+ guides by Cochrane, McCloskey, Shapiro, Head, and other leading economists. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/econ-writing-skill?style=flat-square)
> - **[Econ Paper Review Skill](https://github.com/hanlulong/econ-paper-review-skill)** — AI referee reports for economics papers: verified comments, editing notes, and a step-by-step revision plan before a real referee sees it. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/econ-paper-review-skill?style=flat-square)
> - **[Econ Slides Skill](https://github.com/hanlulong/econ-slides-skill)** — Turn your paper into a professional Beamer talk with a timed speaker script: conference, seminar, job-market, and discussant decks with verified layouts and honest numbers. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/econ-slides-skill?style=flat-square)
> - **[Econ Auto Research](https://github.com/hanlulong/econ-auto-research)** — The vision: an economist-directed AI pipeline from research question to working paper, with adversarial self-refereeing. Star to shape the roadmap. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/econ-auto-research?style=flat-square)
> - **[overleaf-sync-now](https://github.com/hanlulong/overleaf-sync-now)** — Keeps local LaTeX in sync with Overleaf so AI coding agents never edit a stale paper. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/overleaf-sync-now?style=flat-square)

## Contents

- [MCP Servers for Economic Data](#mcp-servers-for-economic-data)
- [Coding Tools for Economists](#coding-tools-for-economists)
- [Causal Inference and Econometrics](#causal-inference-and-econometrics)
- [Simulation, Forecasting and Macro Modeling](#simulation-forecasting-and-macro-modeling)
- [Literature Review and Research Discovery](#literature-review-and-research-discovery)
- [Economic Data and Analysis](#economic-data-and-analysis)
- [Academic Writing and LaTeX](#academic-writing-and-latex)
- [Document Processing and OCR](#document-processing-and-ocr)
- [NLP and Sentiment for Economics](#nlp-and-sentiment-for-economics)
- [Policy, Labor and Alternative Data](#policy-labor-and-alternative-data)
- [Finance-Specific AI](#finance-specific-ai)
- [Data Collection Tools](#data-collection-tools)
- [Papers and Books](#papers-and-books)
- [Courses, Conferences and Community](#courses-conferences-and-community)
- [Appendix: General-Purpose AI](#appendix-general-purpose-ai)

## MCP Servers for Economic Data

[Model Context Protocol](https://modelcontextprotocol.io/) (MCP) servers let AI assistants query economic databases directly. Connect Claude, Cursor, or other MCP-compatible tools to live data from FRED, World Bank, IMF, and more.

- [Alpha Vantage MCP](https://mcp.alphavantage.co/) - Official server for stocks, forex, commodities, and economic indicators.
- [BEA MCP Server](https://github.com/shawndrake2/mcp-bea) - Exposes U.S. Bureau of Economic Analysis data including GDP, personal income, and regional accounts. ![GitHub stars](https://img.shields.io/github/stars/shawndrake2/mcp-bea?style=flat-square)
- [BLS MCP Server](https://github.com/shawndrake2/mcp-bls) - Bureau of Labor Statistics data: CPI, unemployment, employment, and wages via BLS API. ![GitHub stars](https://img.shields.io/github/stars/shawndrake2/mcp-bls?style=flat-square)
- [Census MCP Server](https://lobehub.com/mcp/brockwebb-census-mcp-server) - Natural language queries for U.S. Census demographic data.
- [Data Commons MCP Server](https://github.com/datacommonsorg/agent-toolkit) - Query Data Commons public statistics from Census, World Bank, WHO, and BLS to ground AI answers. ![GitHub stars](https://img.shields.io/github/stars/datacommonsorg/agent-toolkit?style=flat-square)
- [ECB MCP Server](https://github.com/scka-de/ecb-mcp) - Query European Central Bank exchange rates, policy rates, yield curves, and euro-area monetary statistics. ![GitHub stars](https://img.shields.io/github/stars/scka-de/ecb-mcp?style=flat-square)
- [Eurostat MCP Server](https://github.com/ano-kuhanathan/eurostat-mcp) - Query Eurostat APIs for EU statistics with dataset search, filtering, and CSV export. ![GitHub stars](https://img.shields.io/github/stars/ano-kuhanathan/eurostat-mcp?style=flat-square)
- [Financial Datasets MCP](https://github.com/financial-datasets/mcp-server) - Stock market data including prices, financials, and SEC filings via MCP. ![GitHub stars](https://img.shields.io/github/stars/financial-datasets/mcp-server?style=flat-square)
- [FRED MCP Server](https://github.com/stefanoamorelli/fred-mcp-server) - Access all 800,000+ FRED time series with date filtering and frequency adjustment. ![GitHub stars](https://img.shields.io/github/stars/stefanoamorelli/fred-mcp-server?style=flat-square)
- [IMF Data MCP Server](https://github.com/c-cf/imf-data-mcp) - WEO forecasts, balance of payments, and more from the IMF. ![GitHub stars](https://img.shields.io/github/stars/c-cf/imf-data-mcp?style=flat-square)
- [Nasdaq Data Link MCP](https://github.com/stefanoamorelli/nasdaq-data-link-mcp) - Access Nasdaq/Quandl financial and economic datasets. ![GitHub stars](https://img.shields.io/github/stars/stefanoamorelli/nasdaq-data-link-mcp?style=flat-square)
- [OECD MCP Server](https://github.com/isakskogstad/OECD-MCP) - Access 5,000+ OECD statistical datasets via SDMX API with prompt templates. ![GitHub stars](https://img.shields.io/github/stars/isakskogstad/OECD-MCP?style=flat-square)
- [**OpenEcon**](https://openecon.ai/) - Natural language interface to 330,000+ economic indicators across FRED, World Bank, IMF, and more, with CSV, JSON, and DTA export. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/openecon-data?style=flat-square)
- [SEC EDGAR MCP](https://github.com/stefanoamorelli/sec-edgar-mcp) - Connects AI assistants to U.S. SEC EDGAR filings, financial statements, and insider-trading data. ![GitHub stars](https://img.shields.io/github/stars/stefanoamorelli/sec-edgar-mcp?style=flat-square)
- [TAM MCP Server](https://github.com/gvaibhav/TAM-MCP-Server) - One server, eight sources: Alpha Vantage, BLS, Census, FRED, IMF, Nasdaq, OECD, and World Bank. ![GitHub stars](https://img.shields.io/github/stars/gvaibhav/TAM-MCP-Server?style=flat-square)
- [U.S. Census Bureau Data API MCP](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp) - Official Census Bureau server connecting AI assistants to demographic, economic, and population statistics. ![GitHub stars](https://img.shields.io/github/stars/uscensusbureau/us-census-bureau-data-api-mcp?style=flat-square)
- [UN Comtrade MCP Server](https://github.com/cyanheads/un-comtrade-mcp-server) - Access UN Comtrade international trade statistics with country and HS commodity code lookup. ![GitHub stars](https://img.shields.io/github/stars/cyanheads/un-comtrade-mcp-server?style=flat-square)
- [World Bank Data360 MCP](https://github.com/worldbank/data360-mcp) - Official World Bank server giving AI agents structured access to Data360 development indicators. ![GitHub stars](https://img.shields.io/github/stars/worldbank/data360-mcp?style=flat-square)
- [World Bank MCP Server](https://github.com/anshumax/world_bank_mcp_server) - Community server for the legacy World Bank Open Data API (the official one is World Bank Data360 MCP above). ![GitHub stars](https://img.shields.io/github/stars/anshumax/world_bank_mcp_server?style=flat-square)

> Browse the [MCP Registry](https://registry.modelcontextprotocol.io/) to discover more servers.

## Coding Tools for Economists

- [AI-research-setup](https://github.com/hanlulong/AI-research-setup) - Step-by-step guide to setting up Claude Code and Codex for economics research on macOS and Windows. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/AI-research-setup?style=flat-square)
- [Aider](https://github.com/Aider-AI/aider) - AI pair programming in your terminal with git integration and 260+ LLM support. ![GitHub stars](https://img.shields.io/github/stars/Aider-AI/aider?style=flat-square)
- [awesome-econ-ai-stuff](https://github.com/meleantonio/awesome-econ-ai-stuff) - Reusable AI skills for economists (SKILL.md standard) covering Stata, Python, and LaTeX workflows. ![GitHub stars](https://img.shields.io/github/stars/meleantonio/awesome-econ-ai-stuff?style=flat-square)
- [Cline](https://github.com/cline/cline) - Autonomous coding agent for VS Code with Plan/Act modes and MCP integration. ![GitHub stars](https://img.shields.io/github/stars/cline/cline?style=flat-square)
- [Jupyter AI](https://github.com/jupyterlab/jupyter-ai) - Official JupyterLab extension with `%%ai` magic commands for code generation and explanation. ![GitHub stars](https://img.shields.io/github/stars/jupyterlab/jupyter-ai?style=flat-square)
- [Jupyter AI Agents](https://github.com/datalayer/jupyter-ai-agents) - AI agents for JupyterLab with MCP integration for connecting notebooks to FRED, World Bank, and more. ![GitHub stars](https://img.shields.io/github/stars/datalayer/jupyter-ai-agents?style=flat-square)
- [Marimo](https://github.com/marimo-team/marimo) - Reactive Python notebook stored as pure .py files with built-in AI assistant. ![GitHub stars](https://img.shields.io/github/stars/marimo-team/marimo?style=flat-square)
- [opencode](https://github.com/anomalyco/opencode) - Open-source, provider-agnostic AI coding agent built for the terminal with a TUI. ![GitHub stars](https://img.shields.io/github/stars/anomalyco/opencode?style=flat-square)
- [Positron IDE](https://posit.co/products/ide/positron/) - IDE from Posit (makers of RStudio) with native R and Python support and an AI data assistant.
- [**Stata-MCP**](https://github.com/hanlulong/stata-mcp) - Execute .do/.ado/.mata files from VS Code, Cursor, Claude Code, or GitHub Copilot with real-time output panels, built-in data viewer, and graph display. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/stata-mcp?style=flat-square)

### AI Agent Frameworks

_Build automated research pipelines — from data collection to analysis to report generation._

- [Agno](https://github.com/agno-agi/agno) - Open-source Python framework with memory, knowledge, and 100+ toolkits including MCP support. ![GitHub stars](https://img.shields.io/github/stars/agno-agi/agno?style=flat-square)
- [AutoGen](https://github.com/microsoft/autogen) - Microsoft's multi-agent conversation framework for complex research workflows. ![GitHub stars](https://img.shields.io/github/stars/microsoft/autogen?style=flat-square)
- [chatlas](https://posit-dev.github.io/chatlas/) - Posit's Python interface for LLMs with streaming, tool calling, and structured output. ![GitHub stars](https://img.shields.io/github/stars/posit-dev/chatlas?style=flat-square)
- [CrewAI](https://www.crewai.com/) - Role-based multi-agent systems for collaborative research workflows.
- [DeerFlow](https://github.com/bytedance/deer-flow) - ByteDance's research SuperAgent for long-horizon tasks with sandboxed code execution. ![GitHub stars](https://img.shields.io/github/stars/bytedance/deer-flow?style=flat-square)
- [DSPy](https://github.com/stanfordnlp/dspy) - Stanford framework for programmatic LLM optimization — "programming, not prompting." ![GitHub stars](https://img.shields.io/github/stars/stanfordnlp/dspy?style=flat-square)
- [**Econ Auto Research**](https://github.com/hanlulong/econ-auto-research) - Vision stage: an economist-directed research pipeline — identification judgment, pre-specified analysis, and referee-grade self-checking — built on the OpenEcon toolchain. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/econ-auto-research?style=flat-square)
- [ellmer](https://ellmer.tidyverse.org) - Tidyverse R package for calling LLM APIs with tool calling and structured data extraction. ![GitHub stars](https://img.shields.io/github/stars/tidyverse/ellmer?style=flat-square)
- [Google ADK](https://github.com/google/adk-python) - Google's modular multi-agent framework with MCP and A2A protocol support. ![GitHub stars](https://img.shields.io/github/stars/google/adk-python?style=flat-square)
- [GPT Researcher](https://github.com/assafelovic/gpt-researcher) - Autonomous deep research agent producing cited reports from web sources. ![GitHub stars](https://img.shields.io/github/stars/assafelovic/gpt-researcher?style=flat-square)
- [LangGraph](https://langchain-ai.github.io/langgraph/) - Stateful agent workflows built on cyclic graphs.
- [MetaGPT](https://github.com/FoundationAgents/MetaGPT) - Multi-agent framework simulating roles (PM, analyst, engineer) with structured SOPs. ![GitHub stars](https://img.shields.io/github/stars/FoundationAgents/MetaGPT?style=flat-square)
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - Lightweight production-ready multi-agent framework with handoffs and guardrails. ![GitHub stars](https://img.shields.io/github/stars/openai/openai-agents-python?style=flat-square)
- [Pydantic AI](https://ai.pydantic.dev/) - Type-safe agent framework with structured input/output, ideal for working with economic data.
- [smolagents](https://github.com/huggingface/smolagents) - Hugging Face's minimalist agent library where agents write actions as Python code. ![GitHub stars](https://img.shields.io/github/stars/huggingface/smolagents?style=flat-square)
- [The AI Scientist](https://github.com/SakanaAI/AI-Scientist) - Sakana AI framework for fully automated research with LaTeX paper generation and automated reviewing. ![GitHub stars](https://img.shields.io/github/stars/SakanaAI/AI-Scientist?style=flat-square)

## Causal Inference and Econometrics

### Core Libraries

- [awesome-causal-inference](https://github.com/matteocourthoud/awesome-causal-inference) - Curated list of causal inference resources, courses, and tools. ![GitHub stars](https://img.shields.io/github/stars/matteocourthoud/awesome-causal-inference?style=flat-square)
- [causal-learn](https://github.com/py-why/causal-learn) - Causal discovery algorithms (PC, FCI, GES) from the PyWhy ecosystem. ![GitHub stars](https://img.shields.io/github/stars/py-why/causal-learn?style=flat-square)
- [CausalML](https://github.com/uber/causalml) - Uber's uplift modeling and causal inference with machine learning. ![GitHub stars](https://img.shields.io/github/stars/uber/causalml?style=flat-square)
- [CausalPy](https://github.com/pymc-labs/CausalPy) - Bayesian causal inference for quasi-experiments (DiD, synthetic control, RDD) powered by PyMC. ![GitHub stars](https://img.shields.io/github/stars/pymc-labs/CausalPy?style=flat-square)
- [DoubleML](https://docs.doubleml.org/) - Chernozhukov et al. (2018) Double/Debiased ML in Python and R.
- [DoWhy](https://github.com/py-why/dowhy) - End-to-end causal inference: model, identify, estimate, refute. ![GitHub stars](https://img.shields.io/github/stars/py-why/dowhy?style=flat-square)
- [EconML](https://github.com/py-why/EconML) - Microsoft/PyWhy library for heterogeneous treatment effects via Double ML and causal forests. ![GitHub stars](https://img.shields.io/github/stars/py-why/EconML?style=flat-square)
- [grf](https://github.com/grf-labs/grf) - Generalized Random Forests for heterogeneous treatment effects (Athey, Tibshirani, Wager). ![GitHub stars](https://img.shields.io/github/stars/grf-labs/grf?style=flat-square)
- [pyfixest](https://github.com/py-econometrics/pyfixest) - Fast high-dimensional fixed-effects regression in Python with IV, Poisson, and modern difference-in-differences estimators. ![GitHub stars](https://img.shields.io/github/stars/py-econometrics/pyfixest?style=flat-square)

### Frontier Tools

- [Causal-Copilot](https://github.com/Lancelot39/Causal-Copilot) - LLM agent automating end-to-end causal discovery, inference, and reporting from natural-language queries. ![GitHub stars](https://img.shields.io/github/stars/Lancelot39/Causal-Copilot?style=flat-square)
- [CausalAgent](https://github.com/DMIRLAB-Group/CausalAgent) - Multi-agent AI for end-to-end causal inference through conversation. ![GitHub stars](https://img.shields.io/github/stars/DMIRLAB-Group/CausalAgent?style=flat-square)
- [CausalFM](https://github.com/yccm/CausalFM) - Foundation models for causal inference; pre-trained models replace per-problem estimation (ICLR 2026). ![GitHub stars](https://img.shields.io/github/stars/yccm/CausalFM?style=flat-square)
- [CausalMatch](https://github.com/bytedance/CausalMatch) - ByteDance's causal matching engine at industrial scale. ![GitHub stars](https://img.shields.io/github/stars/bytedance/CausalMatch?style=flat-square)
- [CausalPFN](https://github.com/vdblm/CausalPFN) - Prior-fitted transformer for amortized, in-context ATE and CATE estimation without per-dataset retraining. ![GitHub stars](https://img.shields.io/github/stars/vdblm/CausalPFN?style=flat-square)
- [CImpact](https://github.com/Sanofi-Public/CImpact) - Causal impact for time series with frequentist and Bayesian methods. ![GitHub stars](https://img.shields.io/github/stars/Sanofi-Public/CImpact?style=flat-square)
- [contdid](https://github.com/bcallaway11/contdid) - DiD with continuous treatment, by Brantly Callaway. ![GitHub stars](https://img.shields.io/github/stars/bcallaway11/contdid?style=flat-square)
- [diff-diff](https://github.com/igerber/diff-diff) - Scikit-learn-style difference-in-differences library for Python. ![GitHub stars](https://img.shields.io/github/stars/igerber/diff-diff?style=flat-square)
- [differences](https://github.com/bernardodionisi/differences) - Python implementation of Callaway and Sant'Anna staggered difference-in-differences with multiple periods and triple differences. ![GitHub stars](https://img.shields.io/github/stars/bernardodionisi/differences?style=flat-square)
- [DoubleLingo](https://github.com/markov24/DoubleLingo) - Double ML with LLM-based nuisance models for causal inference on unstructured data. ![GitHub stars](https://img.shields.io/github/stars/markov24/DoubleLingo?style=flat-square)
- [moderndid](https://github.com/jordandeklerk/moderndid) - GPU-accelerated modern DiD with staggered adoption and event studies. ![GitHub stars](https://img.shields.io/github/stars/jordandeklerk/moderndid?style=flat-square)
- [pysyncon](https://github.com/sdfordham/pysyncon) - Python synthetic control suite with classic, augmented, penalized, and robust estimators plus placebo inference. ![GitHub stars](https://img.shields.io/github/stars/sdfordham/pysyncon?style=flat-square)
- [Salesforce CausalAI](https://github.com/salesforce/causalai) - Causal analysis for time series and tabular data. ![GitHub stars](https://img.shields.io/github/stars/salesforce/causalai?style=flat-square)
- [scpi](https://nppackages.github.io/scpi/) - Synthetic control with prediction intervals for single, multiple, and staggered-adoption units, in R, Python, and Stata. ![GitHub stars](https://img.shields.io/github/stars/nppackages/scpi?style=flat-square)
- [TexIV](https://github.com/SepineTam/TexIV) - Extract instrumental variables from text data using ML. ![GitHub stars](https://img.shields.io/github/stars/SepineTam/TexIV?style=flat-square)
- [xtdml](https://github.com/POLSEAN/xtdml) - Stata module for double machine learning in static panel models with fixed effects. ![GitHub stars](https://img.shields.io/github/stars/POLSEAN/xtdml?style=flat-square)

## Simulation, Forecasting and Macro Modeling

### Agent-Based Models and LLM Simulation

- [AgentSociety](https://github.com/tsinghua-fib-lab/AgentSociety) - Large-scale LLM-driven social simulator modeling urban, social, and economic spaces with taxation and banking. ![GitHub stars](https://img.shields.io/github/stars/tsinghua-fib-lab/AgentSociety?style=flat-square)
- [BeforeIT.jl](https://github.com/bancaditalia/BeforeIT.jl) - Bank of Italy's agent-based macroeconomic model in Julia. ![GitHub stars](https://img.shields.io/github/stars/bancaditalia/BeforeIT.jl?style=flat-square)
- [Concordia](https://github.com/google-deepmind/concordia) - Google DeepMind library for generative agent-based modeling of social, economic, and market interactions. ![GitHub stars](https://img.shields.io/github/stars/google-deepmind/concordia?style=flat-square)
- [EconAgent](https://github.com/tsinghua-fib-lab/ACL24-EconAgent) - LLM agents with personality traits simulating macroeconomic activities (ACL 2024). ![GitHub stars](https://img.shields.io/github/stars/tsinghua-fib-lab/ACL24-EconAgent?style=flat-square)
- [LLM-ABM Survey](https://github.com/tsinghua-fib-lab/LLM-Agent-Based-Modeling-and-Simulation) - Tsinghua's toolkit and survey for LLM agent-based modeling. ![GitHub stars](https://img.shields.io/github/stars/tsinghua-fib-lab/LLM-Agent-Based-Modeling-and-Simulation?style=flat-square)
- [LLM-Economist](https://github.com/sethkarten/LLM-Economist) - Mechanism design with 3–1,000+ LLM agents for optimal taxation research. ![GitHub stars](https://img.shields.io/github/stars/sethkarten/LLM-Economist?style=flat-square)
- [MarS](https://github.com/microsoft/MarS) - Microsoft engine simulating financial markets via a generative Large Market Model of order flow. ![GitHub stars](https://img.shields.io/github/stars/microsoft/MarS?style=flat-square)

### Forecasting and Nowcasting

- [Chronos](https://github.com/amazon-science/chronos-forecasting) - Amazon's pretrained time series models with Bolt variant for 250x speedup. ![GitHub stars](https://img.shields.io/github/stars/amazon-science/chronos-forecasting?style=flat-square)
- [Durbyn.jl](https://github.com/taf-society/Durbyn.jl) - Julia port of R's forecast package. ![GitHub stars](https://img.shields.io/github/stars/taf-society/Durbyn.jl?style=flat-square)
- [emerging-trajectories](https://github.com/wgryc/emerging-trajectories) - LLM-based forecasting of political and economic events. ![GitHub stars](https://img.shields.io/github/stars/wgryc/emerging-trajectories?style=flat-square)
- [Lag-Llama](https://github.com/time-series-foundation-models/lag-llama) - First open-source foundation model for probabilistic time series forecasting. ![GitHub stars](https://img.shields.io/github/stars/time-series-foundation-models/lag-llama?style=flat-square)
- [neuralforecast](https://github.com/Nixtla/neuralforecast) - Neural forecasting models (N-BEATS, NHITS, Transformers) for economic time series. ![GitHub stars](https://img.shields.io/github/stars/Nixtla/neuralforecast?style=flat-square)
- [Now-Casting.com](https://www.now-casting.com/) - Real-time GDP nowcasts for major economies, updated as data releases occur.
- [Project Spectrum](https://www.bis.org/about/bisih/topics/suptech_regtech/spectrum.htm) - BIS/ECB/Bundesbank GenAI for inflation nowcasting, categorizing 34M+ products for CPI.
- [statsforecast](https://github.com/Nixtla/statsforecast) - Fast statistical forecasting for econometric time series. ![GitHub stars](https://img.shields.io/github/stars/Nixtla/statsforecast?style=flat-square)
- [Sundial](https://github.com/thuml/Sundial) - Generative time-series foundation models giving probabilistic forecasts via flow matching without discrete tokenization. ![GitHub stars](https://img.shields.io/github/stars/thuml/Sundial?style=flat-square)
- [tabpfn-time-series](https://github.com/PriorLabs/tabpfn-time-series) - Zero-shot time-series forecasting that repurposes the TabPFN-v2 tabular foundation model, no training needed. ![GitHub stars](https://img.shields.io/github/stars/PriorLabs/tabpfn-time-series?style=flat-square)
- [TimeGPT](https://github.com/Nixtla/nixtla) - Nixtla's foundation model for time series trained on 100B+ data points. ![GitHub stars](https://img.shields.io/github/stars/Nixtla/nixtla?style=flat-square)
- [TimesFM](https://github.com/google-research/timesfm) - Google's decoder-only time series foundation model pre-trained on 400B+ time points. ![GitHub stars](https://img.shields.io/github/stars/google-research/timesfm?style=flat-square)
- [TiRex](https://github.com/NX-AI/tirex) - NX-AI's xLSTM-based zero-shot time-series foundation model topping the GIFT-Eval forecasting leaderboard. ![GitHub stars](https://img.shields.io/github/stars/NX-AI/tirex?style=flat-square)
- [Toto](https://github.com/DataDog/toto) - Datadog's open-weight time-series foundation model, paired with the 350M-observation BOOM benchmark. ![GitHub stars](https://img.shields.io/github/stars/DataDog/toto?style=flat-square)
- [uni2ts](https://github.com/SalesforceAIResearch/uni2ts) - Unified time series transformer models. ![GitHub stars](https://img.shields.io/github/stars/SalesforceAIResearch/uni2ts?style=flat-square)

### Game Theory and Mechanism Design

- [Axelrod](https://github.com/Axelrod-Python/Axelrod) - Iterated Prisoner's Dilemma research with 200+ strategies and tournament simulations. ![GitHub stars](https://img.shields.io/github/stars/Axelrod-Python/Axelrod?style=flat-square)
- [Nashpy](https://nashpy.readthedocs.io/) - Two-player game solver with support enumeration, vertex enumeration, and Lemke-Howson.
- [pygambit](https://www.gambit-project.org/) - Game theory computation for extensive and strategic form games with a Python API.

### DSGE and Structural Models

- [Deep Learning for Dynamic Econ](https://github.com/sischei/Deep_Learning_For_Dynamic_Econ) - Neural networks to solve DSGE models (course materials).
- [econpizza](https://github.com/gboehl/econpizza) - JAX-based solver for fully nonlinear heterogeneous-agent (HANK) macroeconomic models via automatic differentiation. ![GitHub stars](https://img.shields.io/github/stars/gboehl/econpizza?style=flat-square)
- [gEconpy](https://github.com/jessegrabowski/gEconpy) - DSGE toolkit in Python. ![GitHub stars](https://img.shields.io/github/stars/jessegrabowski/gEconpy?style=flat-square)
- [MacroModelling.jl](https://github.com/thorek1/MacroModelling.jl) - Julia DSGE toolkit. ![GitHub stars](https://img.shields.io/github/stars/thorek1/MacroModelling.jl?style=flat-square)
- [OpenSourceEconomics](https://github.com/OpenSourceEconomics) - JAX-compatible DC-EGM, Kalman filters, and econ-project-templates.
- [optimagic](https://github.com/optimagic-dev/optimagic) - Numerical optimization for economists (formerly estimagic). ![GitHub stars](https://img.shields.io/github/stars/optimagic-dev/optimagic?style=flat-square)

## Literature Review and Research Discovery

- [alphaXiv](https://www.alphaxiv.org/) - Line-by-line discussion on arXiv papers with AI-powered analysis.
- [ASReview](https://github.com/asreview/asreview) - Active learning for systematic reviews, reducing screening time by up to 95% (Nature Machine Intelligence). ![GitHub stars](https://img.shields.io/github/stars/asreview/asreview?style=flat-square)
- [Asta](https://asta.allen.ai/) - Ai2's open agentic-science assistant for paper finding, cited literature synthesis, and data analysis. ![GitHub stars](https://img.shields.io/github/stars/allenai/asta-bench?style=flat-square)
- [Connected Papers](https://www.connectedpapers.com/) - Visual graphs of related papers from a seed paper.
- [Consensus](https://consensus.app/) - Evidence meter categorizing findings as yes/no/mixed across 200M+ papers.
- [Elicit](https://elicit.com/) - Research agents synthesizing up to 80 papers into structured briefs from a large literature corpus.
- [Inciteful](https://inciteful.xyz/) - Free citation network analysis using graph algorithms to find key papers and connections.
- [Kosmos](https://edisonscientific.com/) - Autonomous AI scientist reading 1,500+ papers per run to synthesize fully cited research reports.
- [LangChain Open Deep Research](https://github.com/langchain-ai/open_deep_research) - Open-source configurable deep-research agent producing cited reports across any LLM and search tools. ![GitHub stars](https://img.shields.io/github/stars/langchain-ai/open_deep_research?style=flat-square)
- [Litmaps](https://www.litmaps.com/) - Dynamic multi-seed citation mapping with monitored searches and daily alerts for new papers.
- [Meta-Mar](https://www.meta-mar.com/) - Free meta-analysis platform where AI reads PDFs and extracts quantitative outcomes.
- [MindMap AI](https://mindmapai.app/) - Turns research papers, PDFs, and notes into structured visual mind maps for literature synthesis.
- [OpenAlex](https://openalex.org/) - Fully open catalog of scholarly works with a free REST API and semantic search.
- [OpenScholar](https://github.com/AkariAsai/OpenScholar) - Retrieval-augmented LM for scientific literature synthesis across 45M+ papers (Nature 2026). ![GitHub stars](https://img.shields.io/github/stars/AkariAsai/OpenScholar?style=flat-square)
- [PaperQA2](https://github.com/Future-House/paper-qa) - RAG system for question answering and summarization over scientific literature. ![GitHub stars](https://img.shields.io/github/stars/Future-House/paper-qa?style=flat-square)
- [Rayyan](https://www.rayyan.ai/) - AI screening for systematic reviews with 90% time reduction and PRISMA flowcharts.
- [ResearchRabbit](https://www.researchrabbit.ai/) - Citation network and semantic similarity discovery rebuilt with Litmaps.
- [SciSpace](https://scispace.com/) - Deep review with iterative search and Zotero integration across 280M papers.
- [Scite](https://scite.ai/) - Classifies 1.5B+ citations as supporting or contrasting with AI-driven research rankings.
- [Semantic Scholar](https://www.semanticscholar.org/) - AI-powered academic search with citation analysis, TLDR summaries, and free API across 220M+ papers.
- [STORM](https://github.com/stanford-oval/storm) - Stanford's LLM-powered system that researches topics and generates full reports with citations. ![GitHub stars](https://img.shields.io/github/stars/stanford-oval/storm?style=flat-square)
- [Suppr](https://suppr.ai/) - AI literature search, document translation, and deep-research reports over PubMed and OpenAlex, with a Zotero plugin.
- [Undermind](https://www.undermind.ai/) - Autonomously reads hundreds of papers and produces structured reports with timelines and categories.
- [Zotero PapersGPT](https://github.com/papersgpt/papersgpt-for-zotero) - Zotero AI plugin supporting ChatGPT, Claude, Gemini, and more for PDF chat and summaries. ![GitHub stars](https://img.shields.io/github/stars/papersgpt/papersgpt-for-zotero?style=flat-square)

## Economic Data and Analysis

### AI Data Analysis Platforms

- [Julius AI](https://julius.ai/) - Upload datasets and ask questions in natural language; returns charts, regressions, and reports.
- [Microsoft Data Formulator](https://github.com/microsoft/data-formulator) - Describe charts in English and get publication-quality output with Python code. ![GitHub stars](https://img.shields.io/github/stars/microsoft/data-formulator?style=flat-square)

### Economic Data Sources

- [**OpenEcon Data**](https://openecon.ai/) - Query 330,000+ economic indicators from FRED, World Bank, IMF, Comtrade, StatsCan, Eurostat, BIS, and more in plain English. Export to CSV, JSON, DTA, or Python. [Try it](https://data.openecon.ai) | [GitHub](https://github.com/hanlulong/openecon-data) ![GitHub stars](https://img.shields.io/github/stars/hanlulong/openecon-data?style=flat-square)
- [fedfred](https://github.com/nikhilxsunder/fedfred) - Modern Python client for the FRED API at scale. ![GitHub stars](https://img.shields.io/github/stars/nikhilxsunder/fedfred?style=flat-square)
- [FRED API v2](https://fred.stlouisfed.org/docs/api/fred/) - Bulk retrieval of all series in any release across 800,000+ time series.
- [FXMacroData](https://fxmacrodata.com/) - API and MCP server for macroeconomic releases, calendars, FX, commodities, and bond yields, queryable in plain English.
- [Global Macro Database](https://www.globalmacrodata.com/) - Open-source macro dataset covering 241 countries, 1086–2024, from contemporary and historical sources.
- [Trading Economics API](https://tradingeconomics.com/api/) - 300,000+ indicators from 196 countries with Python and R packages.

## Academic Writing and LaTeX

- [AI Research Feedback](https://github.com/claesbackman/AI-research-feedback) - Claude Code skills giving multi-agent referee-style feedback on economics papers before submission. ![GitHub stars](https://img.shields.io/github/stars/claesbackman/AI-research-feedback?style=flat-square)
- [**Econ Paper Review Skill**](https://github.com/hanlulong/econ-paper-review-skill) - Agent skill producing tough, fair referee reports on economics papers — verified comments, editing notes, and a revision plan. Works with Claude Code and OpenAI Codex. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/econ-paper-review-skill?style=flat-square)
- [**Econ Slides Skill**](https://github.com/hanlulong/econ-slides-skill) - Agent skill turning a paper into a professional Beamer talk plus a timed speaker script — conference, seminar, job-market, and discussant decks with compile-and-render verification. Works with Claude Code and OpenAI Codex. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/econ-slides-skill?style=flat-square)
- [**Econ Writing Skill**](https://github.com/hanlulong/econ-writing-skill) - Agent skill for writing economics papers, synthesizing 50+ guides by Cochrane, McCloskey, Shapiro, Head, and others. Works with Claude Code and OpenAI Codex. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/econ-writing-skill?style=flat-square)
- [OpenAI Prism](https://openai.com/prism/) - Free LaTeX workspace with citation management, Zotero sync, sketch-to-equation, and real-time collaboration.
- [Overleaf AI Assist](https://www.overleaf.com/about/ai-features) - LaTeX error fixing, table generation, and equation generation from prompts or images.
- [overleaf-sync-now](https://github.com/hanlulong/overleaf-sync-now) - Keeps local LaTeX in sync with Overleaf so AI coding agents never edit a stale paper. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/overleaf-sync-now?style=flat-square)
- [Paperpal](https://paperpal.com/) - Academic writing assistant on Overleaf, Google Docs, and Chrome.
- [Refine.ink](https://www.refine.ink/) - AI referee generating peer-review-quality feedback on academic papers, piloting with top economics journals.
- [Rigorous](https://github.com/Agentic-Systems-Lab/rigorous) - Open-source AI pre-submission peer review generating referee-style manuscript feedback using your own LLM keys. ![GitHub stars](https://img.shields.io/github/stars/Agentic-Systems-Lab/rigorous?style=flat-square)
- [Thesify](https://www.thesify.ai/) - AI reviewer evaluating argumentation, methodology, and rigor.
- [Typst](https://typst.app/) - Modern LaTeX alternative with dramatically simpler syntax and sub-second compilation.
- [Underleaf](https://www.underleaf.ai/) - Chrome extension for image-to-LaTeX and smart citation generation.

## Document Processing and OCR

- [DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR) - Open-weight vision model converting document images to Markdown with formula and table recognition. ![GitHub stars](https://img.shields.io/github/stars/deepseek-ai/DeepSeek-OCR?style=flat-square)
- [Docling](https://github.com/docling-project/docling) - IBM open-source document parser with 0.97 table recognition accuracy. ![GitHub stars](https://img.shields.io/github/stars/docling-project/docling?style=flat-square)
- [eScriptorium](https://gitlab.com/scripta/escriptorium) - Open-source platform for segmenting, transcribing, and OCR-ing historical and handwritten manuscripts.
- [Marker](https://github.com/datalab-to/marker) - PDF to Markdown/JSON at 122 pages/sec with multi-page table merging. ![GitHub stars](https://img.shields.io/github/stars/datalab-to/marker?style=flat-square)
- [Mathpix](https://mathpix.com/) - Screenshot-to-LaTeX OCR for equations, tables, and diagrams with PDF-to-Overleaf conversion.
- [MinerU](https://github.com/opendatalab/MinerU) - PDF, web, and e-book content extraction with OCR for 84 languages. ![GitHub stars](https://img.shields.io/github/stars/opendatalab/MinerU?style=flat-square)
- [Mistral OCR 3](https://mistral.ai/news/mistral-ocr-3) - Costs $1–2 per 1,000 pages with support for cursive, complex tables, and low DPI.
- [OlmOCR](https://github.com/allenai/olmocr) - Allen AI's fully open-source OCR with SOTA accuracy on tables, equations, and handwriting. ![GitHub stars](https://img.shields.io/github/stars/allenai/olmocr?style=flat-square)
- [PaddleOCR-VL](https://github.com/PaddlePaddle/PaddleOCR) - Vision-language OCR extracting layout, formulas, and structured tables from documents across many languages. ![GitHub stars](https://img.shields.io/github/stars/PaddlePaddle/PaddleOCR?style=flat-square)
- [Pix2Text](https://github.com/breezedeus/Pix2Text) - Open-source tool recognizing layouts, tables, and math formulas in images, exporting LaTeX and Markdown. ![GitHub stars](https://img.shields.io/github/stars/breezedeus/Pix2Text?style=flat-square)
- [Surya](https://github.com/datalab-to/surya) - Open-source OCR toolkit for 90+ languages with layout, reading-order, and table recognition. ![GitHub stars](https://img.shields.io/github/stars/datalab-to/surya?style=flat-square)
- [Transkribus](https://www.transkribus.org/) - Handwritten historical document transcription with 140+ AI models in 100+ languages.

## NLP and Sentiment for Economics

- [CentralBankRoBERTa](https://github.com/Moritz-Pfeifer/CentralBankRoBERTa) - Fine-tuned RoBERTa for sentiment classification in central bank communications. ![GitHub stars](https://img.shields.io/github/stars/Moritz-Pfeifer/CentralBankRoBERTa?style=flat-square)
- [EconBERTa](https://github.com/worldbank/econberta-econie) - World Bank DeBERTa trained on 9.4B tokens from 1.5M economics papers with NER. ![GitHub stars](https://img.shields.io/github/stars/worldbank/econberta-econie?style=flat-square)
- [FinBERT](https://huggingface.co/ProsusAI/finbert) - Fine-tuned BERT for financial sentiment, widely cited in economics and finance research.
- [FinSentGPT](https://www.sciencedirect.com/science/article/pii/S1057521924002230) - Fine-tuned ChatGPT for multilingual financial sentiment, tested on ECB Monetary Policy Decisions.
- [FinVADER](https://github.com/PetrKorab/FinVADER) - VADER updated with financial lexicons. ![GitHub stars](https://img.shields.io/github/stars/PetrKorab/FinVADER?style=flat-square)
- [GABRIEL](https://github.com/openai/GABRIEL) - OpenAI toolkit turning text, images, or audio into quantitative measures for social scientists. ![GitHub stars](https://img.shields.io/github/stars/openai/GABRIEL?style=flat-square)
- [Llama-3.1-Hawkish-8B](https://huggingface.co/mukaj/Llama-3.1-Hawkish-8B) - Llama-3.1-8B fine-tuned for financial NLP, including hawkish/dovish classification of Fed communications.
- [SentiBigNomics](https://github.com/consose/SentiBigNomics) - Sentiment analysis designed for economic text with aspect-based and negation handling. ![GitHub stars](https://img.shields.io/github/stars/consose/SentiBigNomics?style=flat-square)
- [WorldCentralBanks](https://github.com/gtfintechlab/WorldCentralBanks) - Annotated corpus and per-bank models classifying monetary policy stance in central bank communications worldwide. ![GitHub stars](https://img.shields.io/github/stars/gtfintechlab/WorldCentralBanks?style=flat-square)

## Policy, Labor and Alternative Data

### Policy and Evidence Synthesis

- [EUROMOD](https://euromod-web.jrc.ec.europa.eu/) - EU tax-benefit microsimulation covering all 27 member states (open-source, EUPL-1.2).
- [ImpactAI](https://impactai.worldbank.org/) - World Bank DIME tool synthesizing RCT evidence with effect sizes across interventions.
- [OpenFisca](https://openfisca.readthedocs.io/) - Open-source microsimulation engine for computing taxes and benefits on population data.
- [Plural Policy](https://pluralpolicy.com/) - AI bill summarizer with version comparison and momentum indicators across U.S. jurisdictions.
- [PolicyEngine](https://github.com/PolicyEngine/policyengine-us) - Open-source U.S. tax-benefit microsimulation. ![GitHub stars](https://img.shields.io/github/stars/PolicyEngine/policyengine-us?style=flat-square)

### Labor Market Data

- [Anthropic Economic Index](https://www.anthropic.com/economic-index) - Open dataset and recurring reports mapping which economic tasks and occupations people use AI for.
- [Lightcast](https://lightcast.io/) - 2.5B job postings, 800M profiles, and 160+ countries with AI skills taxonomy.
- [LinkedIn Economic Graph](https://economicgraph.linkedin.com/) - Labor trends, skills migration, and talent matching data for academic researchers.
- [Revelio Labs](https://www.reveliolabs.com/) - 100M+ employment records with academic access via WRDS.

### Spatial, Satellite and Alternative Data

- [CARTO](https://carto.com/) - AI agents that reason with spatial data via natural language.
- [Clay Foundation Model](https://madewithclay.org) - Open foundation model for Earth observation generating embeddings from global multi-sensor satellite imagery. ![GitHub stars](https://img.shields.io/github/stars/Clay-foundation/model?style=flat-square)
- [FlyPix AI](https://flypix.ai/) - No-code custom AI models on satellite and drone imagery for economic measurement.
- [Neudata](https://www.neudata.co/) - Alternative data intelligence cataloging thousands of non-traditional data sources.
- [Overture Maps](https://overturemaps.org) - Open global geospatial data of places, buildings, addresses, and transportation, released monthly. ![GitHub stars](https://img.shields.io/github/stars/OvertureMaps/data?style=flat-square)
- [Stanford Satellite + AI](https://sustainability.stanford.edu/news/satellite-imagery-and-ai-reveal-development-needs-hidden-national-data) - HDI for 61,530 municipalities from satellite imagery (Nature Communications, 2026).

## Finance-Specific AI

- [ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) - Educational multi-agent system mimicking famous investors to research stocks and propose trading decisions. ![GitHub stars](https://img.shields.io/github/stars/virattt/ai-hedge-fund?style=flat-square)
- [awesome-quant](https://github.com/wilsonfreitas/awesome-quant) - Curated quantitative finance resources. ![GitHub stars](https://img.shields.io/github/stars/wilsonfreitas/awesome-quant?style=flat-square)
- [Dexter](https://github.com/virattt/dexter) - Autonomous financial research agent with task planning and real-time data. ![GitHub stars](https://img.shields.io/github/stars/virattt/dexter?style=flat-square)
- [Fin-R1](https://github.com/SUFE-AIFLM-Lab/Fin-R1) - Financial reasoning LLM by Shanghai University of Finance and Economics. ![GitHub stars](https://img.shields.io/github/stars/SUFE-AIFLM-Lab/Fin-R1?style=flat-square)
- [FinGPT](https://github.com/AI4Finance-Foundation/FinGPT) - Open-source financial LLMs for sentiment, forecasting, and reports. ![GitHub stars](https://img.shields.io/github/stars/AI4Finance-Foundation/FinGPT?style=flat-square)
- [FinRobot](https://github.com/AI4Finance-Foundation/FinRobot) - AI agent platform for financial analysis combining LLMs, RL, and quantitative methods. ![GitHub stars](https://img.shields.io/github/stars/AI4Finance-Foundation/FinRobot?style=flat-square)
- [Open Financial LLM Leaderboard](https://huggingface.co/spaces/TheFinAI/Open-FinLLM-Leaderboard) - Public leaderboard benchmarking LLMs across financial NLP, question answering, and forecasting tasks.
- [OpenBB](https://github.com/OpenBB-finance/OpenBB) - Open-source financial research platform with AI copilot and economic data integration. ![GitHub stars](https://img.shields.io/github/stars/OpenBB-finance/OpenBB?style=flat-square)
- [TradingAgents](https://github.com/TauricResearch/TradingAgents) - Multi-agent LLM framework simulating analyst, researcher, trader, and risk-manager roles for trading decisions. ![GitHub stars](https://img.shields.io/github/stars/TauricResearch/TradingAgents?style=flat-square)

## Data Collection Tools

### Web Scraping

- [Crawl4AI](https://github.com/unclecode/crawl4ai) - Open-source web crawler producing LLM-ready markdown for RAG and data pipelines. ![GitHub stars](https://img.shields.io/github/stars/unclecode/crawl4ai?style=flat-square)
- [Crawlee](https://crawlee.dev) - Open-source crawling and scraping library that extracts web data for AI, LLM, and RAG pipelines. ![GitHub stars](https://img.shields.io/github/stars/apify/crawlee?style=flat-square)
- [Firecrawl](https://www.firecrawl.dev/) - Webpages to structured markdown with AI extraction endpoint.
- [Kadoa](https://www.kadoa.com/) - No-code AI extraction for financial and economic data.
- [ScrapeGraphAI](https://github.com/ScrapeGraphAI/Scrapegraph-ai) - LLM-powered scraping that adapts to website changes automatically. ![GitHub stars](https://img.shields.io/github/stars/ScrapeGraphAI/Scrapegraph-ai?style=flat-square)

### Survey and Qualitative Research

- [Anthropic Interviewer](https://www.anthropic.com/research/anthropic-interviewer) - AI-conducted adaptive qualitative interviews at scale across 159 countries.
- [ATLAS.ti](https://atlasti.com/) - AI-powered qualitative coding reducing manual effort by 90%.
- [Conveo](https://conveo.ai/) - AI video interviews with multimodal analysis at scale.
- [Outset AI](https://outset.ai/) - Hundreds of AI-moderated interviews simultaneously in 40+ languages.
- [TheySaid](https://www.theysaid.io) - AI-moderated surveys with conversational follow-ups.

> **Warning:** [Nature](https://www.nature.com/articles/d41586-026-00221-8) reports AI chatbots infiltrating online surveys. Implement detection for MTurk/Prolific studies.

### Synthetic Data

- [Gretel](https://www.nvidia.com/en-us/use-cases/synthetic-data-generation-for-agentic-ai/) - Synthetic data with differential privacy (acquired by NVIDIA in 2025). [Open-source library](https://github.com/gretelai/gretel-synthetics) (archived).
- [MOSTLY AI](https://mostly.ai/) - High-fidelity synthetic datasets with GDPR/HIPAA compliance.
- [SDV](https://github.com/sdv-dev/SDV) - Open-source synthetic data generation with CTGAN, CopulaGAN, and GaussianCopula models. ![GitHub stars](https://img.shields.io/github/stars/sdv-dev/SDV?style=flat-square)
- [Synthcity](https://github.com/vanderschaarlab/synthcity) - Generates and benchmarks synthetic tabular, time-series, and survival data with privacy and fairness metrics. ![GitHub stars](https://img.shields.io/github/stars/vanderschaarlab/synthcity?style=flat-square)

## Papers and Books

### Key Papers

| Paper | Authors | Venue |
|-------|---------|-------|
| [Generative AI for Economic Research](https://www.aeaweb.org/articles?id=10.1257/jel.20231736) | Korinek (2023) | JEL |
| [AI Agents for Economic Research](https://www.nber.org/papers/w34202) | Korinek (2025) | NBER |
| [Deep Learning for Economists](https://www.aeaweb.org/articles?id=10.1257/jel.20241733) | Dell (2025) | JEL |
| [DiD Causal Forests](https://onlinelibrary.wiley.com/doi/abs/10.1002/jae.70001) | Gavrilova et al. (2025) | J. Applied Econometrics |
| [Economics in the Age of Algorithms](https://www.aeaweb.org/articles?id=10.1257%2Fpandp.20251118) | Mullainathan (2025) | AEA P&P |
| [Generative AI at Work](https://academic.oup.com/qje/article/140/2/889/7990658) | Brynjolfsson, Li, Raymond (2025) | QJE |
| [How People Use ChatGPT](https://www.nber.org/papers/w34255) | Chatterji et al. (2025) | NBER |
| [A Research Agenda for the Economics of Transformative AI](https://www.nber.org/papers/w34256) | Brynjolfsson, Korinek, Agrawal (2026) | NBER |
| [LLMs: An Applied Econometric Framework](https://www.nber.org/papers/w33344) | Ludwig, Mullainathan, Rambachan (2025) | NBER |
| [ML Who to Nudge](https://www.gsb.stanford.edu/faculty-research/faculty/susan-athey) | Athey, Keleher, Spiess (2025) | J. Econometrics |
| [The Simple Macroeconomics of AI](https://academic.oup.com/economicpolicy/article-abstract/40/121/13/7728473) | Acemoglu (2025) | Economic Policy |
| [A.I. and Our Economic Future](https://www.nber.org/papers/w34779) | Jones (2026) | NBER |
| [AI in Economics Research](https://onlinelibrary.wiley.com/doi/10.1111/joes.12694) | Bahoo et al. (2025) | J. Economic Surveys |
| [Teaching Economics to the Machines](https://www.nber.org/papers/w34713) | Chen et al. (2026) | NBER |

### Books

- [Deep Learning for Economists](https://dell-research-harvard.github.io/projects/384econdl) - Melissa Dell, JEL 2025 with companion Jupyter notebooks.
- [The Means of Prediction](https://www.amazon.com/Means-Prediction-Really-Works-Benefits-ebook/dp/B0FJ2NZW7D) - Maximilian Kasy on how AI works and who benefits (UChicago Press, 2025).
- [The Scaling Era](https://www.dwarkesh.com/podcast) - Dwarkesh Patel's oral history from Amodei, Hassabis, and Zuckerberg interviews.

## Courses, Conferences and Community

### Courses, Guides and Tutorials

- [AI for Economists](https://sites.google.com/view/lastunen/ai-for-economists) - Jesse Lastunen's prompt-focused templates.
- [AI Tools for Economists and Policy Analysts](https://www.aei.org/technology-and-innovation/ai-tools-for-economists-and-policy-analysts/) - Will Rinehart's (AEI) regularly updated guide mapping AI tools and prompts to economics and policy tasks.
- [Claude Blattman](https://claudeblattman.com/) - Chris Blattman's (UChicago) open-source guide to AI research workflows with Claude Code, no coding required.
- [Claude Code Academic Workflow](https://psantanna.com/claude-code-my-workflow/) - Pedro Sant'Anna's (Emory) ready-to-fork Claude Code template for economics research and teaching.
- [Data Analysis with AI v2.0](https://gabors-data-analysis.com/ai-course/) - Gabor Bekes, CEU Vienna (2026). 12-week course covering LLMs for IV, DiD, and simulations.
- [EconDL](https://dell-research-harvard.github.io/projects/384econdl) - Melissa Dell's Jupyter notebooks for deep learning in economics.
- [Economics of Transformative AI](https://digitaleconomy.stanford.edu/about/education/the-economics-of-transformative-ai/) - Stanford course with slides and exercises.
- [genaiforecon.org](https://www.genaiforecon.org/) - Korinek's companion site with semi-annual updates on tools and techniques.
- [How to Learn and Teach Economics with LLMs](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4391863) - Cowen and Tabarrok's (GMU) practical guide to using GPT for learning, teaching, and researching economics.
- [ML and Causal Inference](https://www.gsb.stanford.edu/faculty-research/labs-initiatives/sil/research/methods/ai-machine-learning/short-course) - Susan Athey, Stanford GSB.
- [ML and Economics at Oxford](https://maxkasy.github.io/home/ML_Econ_Oxford/) - Maximilian Kasy's reading group.
- [Modern AI for Economics Research](https://markusacademy.substack.com/p/modern-ai-for-economics-research) - Markus' Academy talk by Benjamin Golub on Cursor, AI refereeing, and prompting for research.
- [Reflections on Vibe Researching](https://joshuagans.substack.com/p/reflections-on-vibe-researching) - Joshua Gans (Toronto) on where LLMs aid theory work and where human judgment stays essential.
- [Research in the Time of AI](https://paulgp.substack.com/p/research-in-the-time-of-ai) - Paul Goldsmith-Pinkham (Yale) on where AI compresses the research timeline and where taste matters.
- [The Economics of AI](https://www.coursera.org/learn/economics-of-ai) - Korinek, UVA on Coursera.
- [Using AI in Research and Teaching](https://paulgp.substack.com/p/using-ai-in-research-and-teaching) - Paul Goldsmith-Pinkham, Yale SOM.

### Conferences (2025–2026)

- [ESIF Economics and AI+ML](https://www.econometricsociety.org/regional-activities/schedule/2026/06/16/2026-ESIFEconomics-and-AIML-Meeting) - Econometric Society, Cornell, June 2026.
- [IESE Economics of AI](https://www.iese.edu/faculty-research/economics-ai-conference-2026/) - Barcelona, February 2026.
- [NBER AI and Economic Measurement](https://www.nber.org/conferences/ai-and-economic-measurement-spring-2026) - Stanford, May 2026.
- [NBER Digital Economics and AI](https://www.nber.org/conferences/digital-economics-and-ai-meeting-spring-2026) - Spring 2026.
- [NBER Economics of AI](https://www.nber.org/conferences/economics-artificial-intelligence-fall-2026) - Long-running Economics of AI conference, Toronto, September 2026.

### Community

**Newsletters:** [genaiforecon](https://genaiforecon.substack.com/) (Korinek) | [Causal Inference](https://causalinf.substack.com/) (Cunningham) | [Autonomous Econ](https://autonomousecon.substack.com/) (Wong) | [One Useful Thing](https://www.oneusefulthing.org/) (Mollick) | [paulgp](https://paulgp.substack.com/) (Goldsmith-Pinkham) | [Frankly, the Counterfactual](https://franklythecounterfactual.substack.com/) (IU O'Neill)

**Podcasts:** [Dwarkesh Podcast](https://www.dwarkesh.com/podcast) | [Exponential View](https://podcasts.apple.com/us/podcast/azeem-azhars-exponential-view/id1172218725)

**People:** [Anton Korinek](https://genaiforecon.org/) | [Scott Cunningham](https://causalinf.substack.com/) | [Erik Brynjolfsson](https://twitter.com/erikbryn) | [Antonio Mele](https://github.com/meleantonio/awesome-econ-ai-stuff) | [Melissa Dell](https://dell-research-harvard.github.io/) | [Sendhil Mullainathan](https://sendhil.org/)

**Institutions:** [NBER AI](https://www.nber.org/programs-projects/projects-and-centers/economics-digitization) | [Stanford DEL](https://digitaleconomy.stanford.edu/) | [OECD.AI](https://oecd.ai/) | [World Bank ImpactAI](https://impactai.worldbank.org/) | [EconTAI](https://www.econtai.org/)

## Appendix: General-Purpose AI

_Widely known tools listed for completeness with notes on what economists specifically value._

| Tool | Best For (Economists) |
|------|----------------------|
| [ChatGPT](https://chat.openai.com/) | Deep Research mode for analyst-grade reports from 500+ sources |
| [Claude](https://claude.ai/) | Coding (Stata, R, Python), long document analysis (200K context) |
| [Claude Code](https://docs.anthropic.com/en/docs/claude-code) | Agentic terminal coding with [MCP integration](https://github.com/hanlulong/stata-mcp) for Stata and [economic data](https://openecon.ai/) |
| [Cursor](https://cursor.com/) | AI-native code editor with Background Agents |
| [DeepSeek R1](https://huggingface.co/deepseek-ai/DeepSeek-R1) | Open-source (MIT), self-hostable for data privacy |
| [Gemini](https://gemini.google.com/) | Writing, visual reports, Google Workspace integration |
| [GitHub Copilot](https://github.com/features/copilot) | Agent Mode with [RStudio integration](https://docs.posit.co/ide/user/ide/guide/tools/copilot.html) |
| [NotebookLM](https://notebooklm.google.com/) | Document synthesis, Audio Overviews, 1M token context |
| [OpenAI Codex](https://openai.com/codex/) | Parallel task execution with reusable agent skills |
| [Perplexity AI](https://www.perplexity.ai/) | Academic Focus mode filtering for peer-reviewed journals |

## Contributing

Contributions welcome! Read the [contribution guidelines](CONTRIBUTING.md) first.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related or neighboring rights to this work. See [LICENSE](LICENSE).

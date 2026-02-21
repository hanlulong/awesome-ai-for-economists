# Awesome AI for Economists

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

> A curated list of AI tools, platforms, papers, courses, and resources at the intersection of artificial intelligence and economics — for economists, social scientists, and policy analysts.

---

## Contents

- [Korinek's Six Domains Framework](#korineks-six-domains-framework)
- [AI Assistants and Deep Research](#ai-assistants-and-deep-research)
- [Coding and Development Tools](#coding-and-development-tools)
- [MCP Servers for Economic Data](#mcp-servers-for-economic-data)
- [Literature Review and Research Discovery](#literature-review-and-research-discovery)
- [Data Analysis and Visualization](#data-analysis-and-visualization)
- [AI-Enhanced Notebooks](#ai-enhanced-notebooks)
- [Causal Inference and Econometrics](#causal-inference-and-econometrics)
- [Simulation, Forecasting and Macro Modeling](#simulation-forecasting-and-macro-modeling)
- [Finance-Specific AI](#finance-specific-ai)
- [NLP, Sentiment and Text Analysis](#nlp-sentiment-and-text-analysis)
- [Academic Writing and LaTeX](#academic-writing-and-latex)
- [Document Processing and OCR](#document-processing-and-ocr)
- [Spatial, Satellite and Alternative Data](#spatial-satellite-and-alternative-data)
- [Labor Market and Policy Analysis](#labor-market-and-policy-analysis)
- [Web Scraping and Data Collection](#web-scraping-and-data-collection)
- [Survey and Qualitative Research](#survey-and-qualitative-research)
- [Synthetic Data and Privacy](#synthetic-data-and-privacy)
- [Foundational Papers](#foundational-papers)
- [Books](#books)
- [Courses and Conferences](#courses-and-conferences)
- [Blogs, Newsletters and Community](#blogs-newsletters-and-community)
- [Institutional Resources](#institutional-resources)
- [Contributing](#contributing)
- [License](#license)

---

## Korinek's Six Domains Framework

Anton Korinek's 2023 paper *"Generative AI for Economic Research"* ([Journal of Economic Literature](https://www.aeaweb.org/articles?id=10.1257/jel.20231736)) established the canonical framework for how economists can leverage AI. His 2025 follow-up, *"AI Agents for Economic Research"* ([NBER WP 34202](https://www.nber.org/papers/w34202)), extends this to autonomous AI agents.

| Domain | Description | Example Tools |
|--------|-------------|---------------|
| **Ideation** | Brainstorming research questions, identifying gaps, generating hypotheses | ChatGPT, Claude, Gemini |
| **Writing** | Drafting, editing, summarizing, and translating academic text | Prism, Overleaf AI, Paperpal |
| **Literature Review** | Searching, synthesizing, and mapping the academic literature | Elicit, Consensus, Undermind |
| **Data Analysis** | Cleaning, exploring, and analyzing economic datasets | Code Interpreter, Julius AI, NotebookLM |
| **Coding** | Writing, debugging, and optimizing code (Stata, R, Python, Julia) | Claude Code, Cursor, GitHub Copilot |
| **Math** | Deriving equations, checking proofs, solving models symbolically | ChatGPT, Claude, Wolfram Alpha |

---

## AI Assistants and Deep Research

### General-Purpose Assistants

- [ChatGPT](https://chat.openai.com/) — OpenAI's flagship model; best for Deep Research mode that autonomously searches 500+ sources to produce analyst-grade reports.
- [Claude](https://claude.ai/) — Anthropic's assistant; excels at coding, long document analysis (200K context), and careful reasoning.
- [Gemini](https://gemini.google.com/) — Google's model with Deep Research producing interactive visual reports with custom charts and real-time simulations.
- [Perplexity AI](https://www.perplexity.ai/) — AI search engine with Academic Focus mode restricting searches to peer-reviewed journals; partnership with Wiley for publisher content.
- [DeepSeek R1](https://huggingface.co/deepseek-ai/DeepSeek-R1) — Open-source reasoning model (MIT license) with performance comparable to o1; can be self-hosted for data privacy. ![GitHub stars](https://img.shields.io/github/stars/deepseek-ai/DeepSeek-R1?style=flat-square)

### Deep Research Engines

- [OpenAI Deep Research](https://openai.com/index/introducing-deep-research/) — Powered by o3, spends 5-30 min autonomously analyzing sources; produces cited, analyst-grade reports with embedded graphs.
- [Gemini Deep Research](https://gemini.google/overview/deep-research/) — Creates interactive visual reports with charts, diagrams, and simulations; runs on Gemini 2.5 with 1M token context.
- [Perplexity Deep Research](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research) — Multi-step reasoning over academic and web sources; 2-4 min per query.
- [NotebookLM](https://notebooklm.google.com/) — Google's AI notebook with Deep Research, Data Tables (auto-extracts variables into Google Sheets), Audio Overviews, and 1M token context window.

> **Practical comparison:** The [AEI guide](https://www.aei.org/technology-and-innovation/ai-tools-for-economists-and-policy-analysts/) recommends ChatGPT for deep research, Claude for coding, Gemini for writing/copyediting.

---

## Coding and Development Tools

### AI-Native Editors and Agents

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) — Anthropic's agentic CLI; manages full project architecture, git workflows, and multi-file edits from terminal. [Scott Cunningham](https://causalinf.substack.com/p/claude-code-changed-how-i-work-part) and [Korinek](https://www.nber.org/papers/w34202) highlight it as transformative for economists.
- [Cursor](https://cursor.com/) — AI-native code editor (VS Code fork) with Background Agents; crossed $500M ARR, valued at $10B.
- [GitHub Copilot](https://github.com/features/copilot) — AI pair programmer with new Agent Mode and Coding Agent (autonomous background PR creation); [integrated into RStudio](https://docs.posit.co/ide/user/ide/guide/tools/copilot.html).
- [OpenAI Codex](https://openai.com/codex/) — Cloud-based coding agent running tasks in parallel; supports reusable "agent skills" for econometric workflows. [Open-source CLI](https://github.com/openai/codex) available.
- [Google Antigravity](https://developers.googleblog.com/build-with-google-antigravity-our-new-agentic-development-platform/) — Agent-first IDE (Nov 2025) from the Windsurf acquisition; powered by Gemini 3, free in preview.
- [Amazon Kiro](https://kiro.dev/) — Agentic IDE with spec-driven development mode; generates and maintains project plans automatically. Free in preview.

### Economist-Specific Coding Tools

- [Stata-MCP](https://github.com/hanlulong/stata-mcp) — MCP server integrating Stata with AI assistants (Claude, Copilot, Cursor); real-time Stata output in editor, full syntax support for .do/.ado/.mata files. ![GitHub stars](https://img.shields.io/github/stars/hanlulong/stata-mcp?style=flat-square)
- [Positron IDE](https://posit.co/products/ide/positron/) — Next-gen IDE from Posit (makers of RStudio); supports R and Python natively with "Positron Assistant" — a data-science-aware AI that understands your loaded data, plots, and session context.
- [awesome-econ-ai-stuff](https://github.com/meleantonio/awesome-econ-ai-stuff) — Reusable AI skills for economists following the SKILL.md standard; works with Claude Code, Cursor, Codex, Gemini CLI. Covers Stata, Python, LaTeX workflows. ![GitHub stars](https://img.shields.io/github/stars/meleantonio/awesome-econ-ai-stuff?style=flat-square)

### Open-Source Coding Agents

- [Cline](https://cline.bot) — Top open-source coding agent for VS Code; model-agnostic, MCP-compatible, with human-in-the-loop approvals.
- [Aider](https://aider.chat) — Terminal-based AI pair programmer; treats git as first-class citizen with auto-commits.
- [Continue.dev](https://continue.dev) — Open-source IDE extension (20K+ stars) with custom assistant sharing.
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) — Fully open-source autonomous coding agent (formerly OpenDevin). ![GitHub stars](https://img.shields.io/github/stars/All-Hands-AI/OpenHands?style=flat-square)

---

## MCP Servers for Economic Data

The [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) lets AI assistants directly query economic databases via natural language. This is a paradigm shift for data access.

- [FRED MCP Server](https://github.com/stefanoamorelli/fred-mcp-server) — Access all 800,000+ FRED time series; search, browse categories/releases, retrieve filtered observations. ![GitHub stars](https://img.shields.io/github/stars/stefanoamorelli/fred-mcp-server?style=flat-square)
- [World Bank MCP Server](https://github.com/anshumax/world_bank_mcp_server) — Query World Bank Open Data API for development indicators across countries. ![GitHub stars](https://img.shields.io/github/stars/anshumax/world_bank_mcp_server?style=flat-square)
- [IMF Data MCP Server](https://github.com/c-cf/imf-data-mcp) — Access IMF economic data repository for WEO forecasts, balance of payments, and more.
- [TAM MCP Server](https://github.com/gvaibhav/TAM-MCP-Server) — One server integrating 8 economic data sources: Alpha Vantage, BLS, Census, FRED, IMF, Nasdaq, OECD, and World Bank. 28 tools, 15 business prompts.
- [Nasdaq Data Link MCP](https://github.com/stefanoamorelli/nasdaq-data-link-mcp) — Access Nasdaq/Quandl financial and economic datasets; being submitted to JOSS for peer review.
- [Alpha Vantage MCP](https://mcp.alphavantage.co/) — Official vendor-maintained MCP server for financial and economic data (stocks, forex, commodities, economic indicators).
- [Census MCP Server](https://lobehub.com/mcp/brockwebb-census-mcp-server) — Natural language queries for U.S. Census demographic data.
- [OpenEcon](https://openecon.ai/) — AI platform querying FRED, World Bank, IMF, Comtrade, StatsCan, Eurostat, BIS, and ExchangeRate-API via natural language.
- [Stata-MCP](https://github.com/hanlulong/stata-mcp) — Bridge between Stata and AI coding assistants via MCP.

> **Discovery:** Browse the [MCP Registry](https://registry.modelcontextprotocol.io/) (launched Sept 2025) to find additional servers.

---

## Literature Review and Research Discovery

- [Elicit](https://elicit.com/) — Research Agents (Dec 2025) autonomously investigate topics and synthesize up to 80 papers into a single brief; 99.4% data extraction accuracy. 138M papers, Claude Opus-powered.
- [Consensus](https://consensus.app/) — GPT-5-powered Scholar Agent with "Consensus Meter" that categorizes evidence as yes/no/mixed and visualizes the distribution. 200M+ papers.
- [ResearchRabbit](https://www.researchrabbit.ai/) — Rebuilt Oct 2025 with Litmaps integration; now combines citation networks AND semantic similarity for discovery.
- [Undermind](https://www.undermind.ai/) — Deep academic search that autonomously reads hundreds of papers; produces structured reports with timeline, categories, and foundational work. 10 free searches/month.
- [Scite](https://scite.ai/) — Classifies 1.5B+ citations as "supporting" or "contrasting." New: Scite Rankings (first AI-driven research ranking) and patent search across 200M+ patent families.
- [alphaXiv](https://www.alphaxiv.org/) — Line-by-line discussion layer on arXiv papers; AI-powered paper analysis, community spaces. Endorsed by Stanford AI Lab.
- [SciSpace](https://typeset.io/) — Deep Review with multi-step iterative search; agent capabilities and Zotero integration. 280M papers.
- [Connected Papers](https://www.connectedpapers.com/) — Visual graphs of papers related to a seed paper, revealing clusters and influential works.
- [Semantic Scholar](https://www.semanticscholar.org/) — Allen Institute's AI-powered academic search with TLDR summaries and citation context.

---

## Data Analysis and Visualization

### AI Data Analysis Platforms

- [Julius AI](https://julius.ai/) — Upload datasets and ask questions in natural language; returns charts, regressions, and reports. Supports R, Python, SQL. 2M+ users.
- [OpenEcon](https://openecon.ai/) — Purpose-built for economists; query "Show me US GDP vs Germany 2010-2024" and get instant charts from FRED, World Bank, IMF, and more.
- [ChatGPT Code Interpreter](https://chat.openai.com/) — Upload CSV/Excel for exploratory analysis, visualization, and statistical modeling in Python.
- [Microsoft Data Formulator](https://github.com/microsoft/data-formulator) — Free, open-source AI visualization from Microsoft Research; describe charts in English, get publication-quality output with full Python code transparency. ![GitHub stars](https://img.shields.io/github/stars/microsoft/data-formulator?style=flat-square)
- [Hal9](https://hal9.com/) — Chat with databases in natural language; generates SQL and Python behind the scenes. Build custom chatbots on research databases.

### Economic Data Sources

- [FRED API v2](https://fred.stlouisfed.org/docs/api/fred/) — Launched Nov 2025; bulk retrieval of all series in any release with full history. 800,000+ time series. Free.
- [Global Macro Database](https://www.globalmacrodata.com/) — World's most comprehensive open-source macro stats: 241 countries, 1086-2024, 27 contemporary + 84 historical sources.
- [World Bank Open Data](https://data.worldbank.org/) — Free access to global development data covering GDP, poverty, trade, health, and education.
- [Trading Economics API](https://tradingeconomics.com/api/) — 300,000+ economic indicators from 196 countries with Python/R packages.
- [fedfred](https://github.com/nsunder724/fedfred) — Modern Python client for FRED API, designed for bulk macroeconomic data access at scale.

### Visualization

- [Tableau AI](https://www.tableau.com/products/artificial-intelligence) — AI-driven forecasting with auto-model selection, adaptive clustering, and Tableau Pulse for proactive insights.
- [Observable](https://observablehq.com/) — By the creator of D3.js; AI Canvases for collaborative data exploration with inspectable, editable queries.

---

## AI-Enhanced Notebooks

- [Marimo](https://github.com/marimo-team/marimo) — Reactive Python notebook stored as pure .py files (git-friendly); AI-native with Copilot built in. Solves the reproducibility crisis in notebook research. Acquired by CoreWeave. ![GitHub stars](https://img.shields.io/github/stars/marimo-team/marimo?style=flat-square)
- [Hex](https://hex.tech/) — Collaborative analytics with Threads (conversational interface) and Notebook Agent that generates multi-cell SQL/Python/chart chains.
- [Deepnote](https://deepnote.com/) — Went open-source in 2025; AI code completion on all plans. Pro at $9/month includes unlimited AI plus $130/month compute credits.
- [Jupyter AI](https://github.com/jupyterlab/jupyter-ai) — Official JupyterLab extension; `%%ai` magic commands for generating/explaining/fixing code. Supports OpenAI, Anthropic, Hugging Face. ![GitHub stars](https://img.shields.io/github/stars/jupyterlab/jupyter-ai?style=flat-square)
- [Jupyter AI Agents](https://github.com/datalayer/jupyter-ai-agents) — CLI commands for JupyterLab using Pydantic AI agents with MCP integration (connect to FRED, World Bank, etc.).
- [NotebookLM](https://notebooklm.google.com/) — Google's AI notebook with Deep Research, Data Tables, and 1M token context; converts sources into structured slide decks.

---

## Causal Inference and Econometrics

### Core Libraries

- [EconML](https://github.com/py-why/EconML) — Microsoft/py-why library for ML-based causal inference: Double ML, causal forests, heterogeneous treatment effects. ![GitHub stars](https://img.shields.io/github/stars/py-why/EconML?style=flat-square)
- [DoWhy](https://github.com/py-why/dowhy) — End-to-end causal inference: model, identify, estimate, refute. AWS contributed novel causal attribution algorithms. ![GitHub stars](https://img.shields.io/github/stars/py-why/dowhy?style=flat-square)
- [CausalML](https://github.com/uber/causalml) — Uber's package for uplift modeling and causal inference with ML. ![GitHub stars](https://img.shields.io/github/stars/uber/causalml?style=flat-square)
- [DoubleML](https://docs.doubleml.org/) — Implements Chernozhukov et al. (2018) Double/Debiased ML framework; Python and R packages. Training via [Economic AI](https://economicai.com/).
- [awesome-causal-inference](https://github.com/matteocourthoud/awesome-causal-inference) — The definitive curated resource list for causal inference. ![GitHub stars](https://img.shields.io/github/stars/matteocourthoud/awesome-causal-inference?style=flat-square)

### New and Frontier Tools

- [diff-diff](https://github.com/igerber/diff-diff) — sklearn-style Difference-in-Differences library (Jan 2026); fills a critical gap in Python's causal inference ecosystem. ![GitHub stars](https://img.shields.io/github/stars/igerber/diff-diff?style=flat-square)
- [contdid](https://github.com/bcallaway11/contdid) — DiD with continuous treatment, by Brantly Callaway (co-author of the Callaway & Sant'Anna estimator). ![GitHub stars](https://img.shields.io/github/stars/bcallaway11/contdid?style=flat-square)
- [moderndid](https://github.com/jordandeklerk/moderndid) — GPU-accelerated Python library for modern DiD methods (staggered adoption, event studies). ![GitHub stars](https://img.shields.io/github/stars/jordandeklerk/moderndid?style=flat-square)
- [CausalMatch](https://github.com/bytedance/CausalMatch) — ByteDance's internal causal matching engine, integrating ML and econometrics for automated decision-making at scale. ![GitHub stars](https://img.shields.io/github/stars/bytedance/CausalMatch?style=flat-square)
- [CausalFM](https://github.com/yccm/CausalFM) — Foundation models for causal inference via Prior-Data Fitted Networks (ICLR 2026). Pre-trained models replace per-problem estimation. ![GitHub stars](https://img.shields.io/github/stars/yccm/CausalFM?style=flat-square)
- [CausalAgent](https://github.com/DMIRLAB-Group/CausalAgent) — Multi-agent AI system for end-to-end causal inference through conversation (Jan 2026).
- [CImpact](https://github.com/Sanofi-Public/CImpact) — Sanofi's causal impact library for time series; frequentist and Bayesian approaches. ![GitHub stars](https://img.shields.io/github/stars/Sanofi-Public/CImpact?style=flat-square)
- [Salesforce CausalAI](https://github.com/salesforce/causalai) — Open-source causal analysis for time series and tabular data. ![GitHub stars](https://img.shields.io/github/stars/salesforce/causalai?style=flat-square)
- [DoubleLingo](https://github.com/markov24/DoubleLingo) — Double ML with LLM-based nuisance models; opens causal inference to unstructured data.
- [TexIV](https://github.com/SepineTam/TexIV) — ML-based package for extracting instrumental variables from text data.

---

## Simulation, Forecasting and Macro Modeling

### Agent-Based Models and LLM Simulation

- [BeforeIT.jl](https://github.com/bancaditalia/BeforeIT.jl) — Bank of Italy's high-performance ABM macroeconomics package in Julia; institutional-quality ABM code, open-source. ![GitHub stars](https://img.shields.io/github/stars/bancaditalia/BeforeIT.jl?style=flat-square)
- [LLM-Economist](https://github.com/sethkarten/LLM-Economist) — Mechanism design with LLM agents (3 to 1,000+ agents); supports GPT, Claude, Gemini, Llama. Tackles optimal taxation. ![GitHub stars](https://img.shields.io/github/stars/sethkarten/LLM-Economist?style=flat-square)
- [EconAgent](https://github.com/tsinghua-fib-lab/ACL24-EconAgent) — LLM-powered agents with personality traits and memory simulating macro activities (ACL 2024). ![GitHub stars](https://img.shields.io/github/stars/tsinghua-fib-lab/ACL24-EconAgent?style=flat-square)
- [LLM-ABM Survey](https://github.com/tsinghua-fib-lab/LLM-Agent-Based-Modeling-and-Simulation) — Tsinghua's comprehensive toolkit for LLM agent-based modeling covering economic, social, and policy simulation. ![GitHub stars](https://img.shields.io/github/stars/tsinghua-fib-lab/LLM-Agent-Based-Modeling-and-Simulation?style=flat-square)
- [AI Economist](https://github.com/salesforce/ai-economist) — Salesforce RL framework for economic policy design (taxation, redistribution). ![GitHub stars](https://img.shields.io/github/stars/salesforce/ai-economist?style=flat-square)

### Forecasting and Nowcasting

- [Now-Casting.com](https://www.now-casting.com/) — Real-time GDP forecasts for major economies, updated as data releases occur. Academic-grade by methodology pioneers.
- [Project Spectrum](https://www.bis.org/about/bisih/topics/suptech_regtech/spectrum.htm) — BIS/ECB/Bundesbank using GenAI to categorize 34M+ product descriptions for inflation nowcasting. First major central bank deployment of GenAI for CPI.
- [Chronos](https://github.com/amazon-science/chronos-forecasting) — Amazon's pretrained time series forecasting models; Chronos-Bolt variant is 250x faster. ![GitHub stars](https://img.shields.io/github/stars/amazon-science/chronos-forecasting?style=flat-square)
- [statsforecast](https://github.com/Nixtla/statsforecast) — Fast statistical forecasting models for econometric time series. ![GitHub stars](https://img.shields.io/github/stars/Nixtla/statsforecast?style=flat-square)
- [uni2ts](https://github.com/SalesforceAIResearch/uni2ts) — Salesforce's unified time series transformer models. ![GitHub stars](https://img.shields.io/github/stars/SalesforceAIResearch/uni2ts?style=flat-square)
- [Durbyn.jl](https://github.com/taf-society/Durbyn.jl) — Julia port of R's legendary `forecast` package, with better performance for large-scale computation.
- [emerging-trajectories](https://github.com/wgryc/emerging-trajectories) — LLM-based forecasting of political, economic, and social events. ![GitHub stars](https://img.shields.io/github/stars/wgryc/emerging-trajectories?style=flat-square)

### DSGE and Structural Models

- [MacroModelling.jl](https://github.com/thorek1/MacroModelling.jl) — Julia DSGE macro modeling toolkit, growing fast. ![GitHub stars](https://img.shields.io/github/stars/thorek1/MacroModelling.jl?style=flat-square)
- [Deep Learning for Dynamic Econ](https://github.com/sischei/Deep_Learning_For_Dynamic_Econ) — Course materials: neural networks to solve DSGE and dynamic stochastic models.
- [gEconpy](https://github.com/jessegrabowski/gEconpy) — Active DSGE toolkit in Python. ![GitHub stars](https://img.shields.io/github/stars/jessegrabowski/gEconpy?style=flat-square)
- [OpenSourceEconomics](https://github.com/OpenSourceEconomics) — JAX-compatible DC-EGM, Kalman filters, econ-project-templates for reproducible research.
- [optimagic](https://github.com/optimagic-dev/optimagic) — Numerical optimization for economists (rebranded from estimagic). ![GitHub stars](https://img.shields.io/github/stars/optimagic-dev/optimagic?style=flat-square)

---

## Finance-Specific AI

- [FinGPT](https://github.com/AI4Finance-Foundation/FinGPT) — Open-source financial LLMs for sentiment analysis, forecasting, and report generation. ![GitHub stars](https://img.shields.io/github/stars/AI4Finance-Foundation/FinGPT?style=flat-square)
- [Fin-R1](https://github.com/SUFE-AIFLM-Lab/Fin-R1) — Financial reasoning LLM by Shanghai University of Finance and Economics; purpose-trained for economic/financial reasoning. ![GitHub stars](https://img.shields.io/github/stars/SUFE-AIFLM-Lab/Fin-R1?style=flat-square)
- [ClaudeCode-Finance](https://github.com/weklica/ClaudeCode-Finance) — Autonomous agent for deep financial research; "Claude Code built for finance."
- [Dexter](https://github.com/virattt/dexter) — Autonomous financial research agent with task planning, self-reflection, and real-time market data. ![GitHub stars](https://img.shields.io/github/stars/virattt/dexter?style=flat-square)
- [awesome-quant](https://github.com/wilsonfreitas/awesome-quant) — Curated list of quantitative finance libraries and resources. ![GitHub stars](https://img.shields.io/github/stars/wilsonfreitas/awesome-quant?style=flat-square)
- [awesome-ai-in-finance](https://github.com/georgezouq/awesome-ai-in-finance) — ML and AI applications in financial markets. ![GitHub stars](https://img.shields.io/github/stars/georgezouq/awesome-ai-in-finance?style=flat-square)

---

## NLP, Sentiment and Text Analysis

- [SentiBigNomics](https://github.com/consose/SentiBigNomics) — Open-source sentiment analysis designed specifically for economic and financial text; aspect-based, with negation handling and tense detection.
- [FinBERT](https://huggingface.co/ProsusAI/finbert) — Fine-tuned BERT for financial sentiment; widely cited in economics and finance research.
- [FinVADER](https://github.com/PetrKorab/FinVADER) — VADER sentiment classifier updated with financial lexicons. ![GitHub stars](https://img.shields.io/github/stars/PetrKorab/FinVADER?style=flat-square)
- [FinSentGPT](https://www.sciencedirect.com/science/article/pii/S1057521924002230) — Fine-tuned ChatGPT for financial sentiment prediction; multilingual, tested on U.S. media and ECB Monetary Policy Decisions.

---

## Academic Writing and LaTeX

- [OpenAI Prism](https://prism.openai.com/) — Free LaTeX workspace powered by GPT-5.2 (launched Jan 2026). Manages citations, converts Stata/R output to publication-ready tables, turns whiteboard photos into equations. [Featured for economists](https://econ-jobs.com/media/openai-prism-ai-economists-research-papers/).
- [Overleaf AI Assist](https://www.overleaf.com/about/ai-features) — Launched June 2025 for 20M+ Overleaf users; AI language feedback, LaTeX error fixing, table/equation generation from prompts or images.
- [Underleaf](https://www.underleaf.ai/) — Chrome extension for Overleaf: image-to-LaTeX conversion (handwritten equations to code), smart citation generation.
- [Paperpal](https://paperpal.com/) — Academic writing assistant on Overleaf, Google Docs, and Chrome; 3M+ users. Includes AI Disclosure templates for ethical compliance.
- [Thesify](https://www.thesify.ai/) — AI academic reviewer that evaluates argumentation, methodology, and rigor like an expert reviewer.
- [Gamma](https://gamma.app/) — AI presentation creation from prompts or PDFs; supports formatted citations (APA, MLA, Chicago).

---

## Document Processing and OCR

- [Docling](https://github.com/docling-project/docling) — IBM's open-source document AI with Granite-Docling-258M model; 0.97 table recognition accuracy. Handles tables, equations, code. Apache-2.0. ![GitHub stars](https://img.shields.io/github/stars/docling-project/docling?style=flat-square)
- [Marker](https://github.com/datalab-to/marker) — PDF to Markdown/JSON at 122 pages/sec; handles tables, math, and multi-page table merging. Free for research. ![GitHub stars](https://img.shields.io/github/stars/datalab-to/marker?style=flat-square)
- [Mistral OCR 3](https://mistral.ai/news/mistral-ocr-3) — State-of-the-art document parsing at $1-2/1,000 pages; handles cursive, complex tables, low DPI. Up to 97% cheaper than AWS Textract.
- [Transkribus](https://www.transkribus.org/) — Leading platform for handwritten historical document transcription; 140+ public AI models, 100+ languages. Essential for economic history.

---

## Spatial, Satellite and Alternative Data

### Spatial and GIS

- [CARTO Agentic GIS](https://carto.com/) — AI agents that understand natural language and reason with spatial data (Q4 2025); ask "Find optimal locations for housing near transit with low flood risk" and get suitability maps.
- [Esri ArcGIS GeoAI](https://www.esri.com/en-us/geospatial-artificial-intelligence/overview) — 75+ pretrained AI models, no-code automation, AI-powered natural language interaction with spatial data.

### Satellite Imagery

- [FlyPix AI](https://flypix.ai/) — No-code platform for custom AI models on satellite/drone imagery; object detection and pattern recognition without programming.
- [Stanford Satellite + AI](https://sustainability.stanford.edu/news/satellite-imagery-and-ai-reveal-development-needs-hidden-national-data) — Estimated HDI for 61,530 municipalities using satellite imagery and ML (Nature Communications, Feb 2026).

### Alternative Data

- [Neudata](https://www.neudata.co/) — Leading alternative data intelligence platform; catalogs thousands of non-traditional data sources ($15.4B market in 2025).
- [Kadoa](https://www.kadoa.com/) — No-code AI platform for alternative data extraction; specifically designed for financial and economic data.

---

## Labor Market and Policy Analysis

### Labor Market Data

- [Revelio Labs](https://www.reveliolabs.com/) — Universal HR database from 100M+ employment records; available through WRDS for academics. Launched RPLS (Revelio Public Labor Statistics) in 2025.
- [Lightcast](https://lightcast.io/) — 2.5B job postings, 800M career profiles, 100+ government sources across 160+ countries. AI-powered skills taxonomy.
- [LinkedIn Economic Graph](https://economicgraph.linkedin.com/) — Global labor market trends, skills migration, talent matching. Free for academic researchers via the Research Program.

### Policy Analysis and Evidence Synthesis

- [ImpactAI](https://impactai.worldbank.org/) — World Bank DIME's open-source tool using GenAI to synthesize causal policy research (RCTs). Ask "what interventions improve school attendance in Sub-Saharan Africa?" and get evidence summaries with effect sizes. Free.
- [Plural Policy](https://pluralpolicy.com/) — AI bill summarizer with version comparison, momentum indicators, and automatic topic detection across all U.S. jurisdictions.
- [Meta-Mar](https://www.meta-mar.com/) — Free, open-source meta-analysis platform; AI Data Extractor reads PDFs and extracts quantitative outcomes. 5,800+ researchers, 200+ published papers.
- [Rayyan](https://www.rayyan.ai/) — AI screening for systematic reviews; reduces screening time by 90%, 97-99% sensitivity. Auto-generates PRISMA flowcharts. 1M+ researchers.
- [PolicyEngine](https://github.com/PolicyEngine/policyengine-us) — Open-source U.S. tax-benefit microsimulation for policy analysis. ![GitHub stars](https://img.shields.io/github/stars/PolicyEngine/policyengine-us?style=flat-square)

---

## Web Scraping and Data Collection

- [ScrapeGraphAI](https://github.com/ScrapeGraphAI/Scrapegraph-ai) — Open-source LLM-powered scraping with graph-based pipelines; adapts to website changes automatically. ![GitHub stars](https://img.shields.io/github/stars/ScrapeGraphAI/Scrapegraph-ai?style=flat-square)
- [Firecrawl](https://www.firecrawl.dev/) — Converts webpages to structured markdown; `/extract` endpoint uses AI to pull structured data. Free for 500 pages.
- [Kadoa](https://www.kadoa.com/) — No-code AI data extraction focused on financial and economic data. Free tier (500 credits).
- [Octoparse](https://www.octoparse.com/) — 50,000+ students and researchers use it; AI auto-detection of page structure.

---

## Survey and Qualitative Research

### AI-Enhanced Surveys

- [Qualtrics XM](https://www.qualtrics.com/) — AI-powered survey design, real-time sentiment detection, entity recognition, intent classification. Academic pricing available.
- [SurveyMonkey AI](https://www.surveymonkey.com/product/features/ai/) — Purpose-built AI trained on decades of survey science; generates optimized questions and analyzes open-ended responses.
- [TheySaid](https://www.theysaid.io) — AI-moderated surveys with conversational follow-up questions; combines survey breadth with interview depth.

### Qualitative Research AI

- [Outset AI](https://outset.ai/) — Conducts hundreds of AI-moderated interviews simultaneously via video, voice, or text in 40+ languages. Raised $21M.
- [Conveo](https://conveo.ai/) — AI video interviews with multimodal analysis (voice, tone, behavior); 100x faster than traditional qualitative at 75% lower cost.
- [ATLAS.ti](https://atlasti.com/) — AI Coding using GPT for human-level NLU; reduces manual coding by up to 90%.

> **Warning:** [Nature](https://www.nature.com/articles/d41586-026-00221-8) reports AI chatbots are infiltrating online surveys with humanlike behavior. Implement AI detection strategies for MTurk/Prolific studies.

---

## Synthetic Data and Privacy

- [Gretel](https://www.gretel.ai/) — Synthetic data with differential privacy guarantees; acquired by NVIDIA (March 2025). [Open-source library](https://github.com/gretelai/gretel-synthetics) available.
- [MOSTLY AI](https://mostly.ai/) — High-fidelity synthetic datasets preserving statistical patterns; GDPR/HIPAA compliant. Free tier.
- [Alan Turing Institute](https://www.turing.ac.uk/research/research-projects/synthetic-data-generation-finance-and-economics) — Active research on synthetic data methods tailored for finance and economics applications.
- [Koenecke & Varian (2020)](https://arxiv.org/abs/2011.01374) — Foundational paper: no significant difference between results from synthetic vs. real data using Synthetic Data Vault.

---

## Foundational Papers

### Canonical References

| Paper | Authors | Venue |
|-------|---------|-------|
| [Generative AI for Economic Research](https://www.aeaweb.org/articles?id=10.1257/jel.20231736) | Korinek (2023) | Journal of Economic Literature |
| [AI Agents for Economic Research](https://www.nber.org/papers/w34202) | Korinek (2025) | NBER Working Paper |
| [Large Language Models: An Applied Econometric Framework](https://www.nber.org/papers/w33344) | Ludwig, Mullainathan, Rambachan (2025) | NBER Working Paper |
| [Deep Learning for Economists](https://www.aeaweb.org/articles?id=10.1257/jel.20241733) | Melissa Dell (2025) | Journal of Economic Literature |
| [Economics in the Age of Algorithms](https://www.aeaweb.org/articles?id=10.1257%2Fpandp.20251118) | Sendhil Mullainathan (2025) | AEA Papers and Proceedings |
| [Generative AI at Work](https://academic.oup.com/qje/article/140/2/889/7990658) | Brynjolfsson, Li, Raymond (2025) | Quarterly Journal of Economics |
| [The Simple Macroeconomics of AI](https://academic.oup.com/economicpolicy/article-abstract/40/121/13/7728473) | Daron Acemoglu (2025) | Economic Policy |
| [A.I. and Our Economic Future](https://www.nber.org/papers/w34779) | Charles I. Jones (2026) | NBER Working Paper |

### Methodology and Reviews

| Paper | Authors | Venue |
|-------|---------|-------|
| [How to Learn and Teach Economics with LLMs](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4391863) | Cowen & Tabarrok | SSRN |
| [Large Language Models: A Primer for Economists](https://www.bis.org/publ/work1218.htm) | BIS (2024) | BIS Working Papers |
| [AI in Economics Research](https://onlinelibrary.wiley.com/doi/10.1111/joes.12694) | Bahoo et al. (2025) | Journal of Economic Surveys |
| [Teaching Economics to the Machines](https://www.nber.org/papers/w34713) | Chen et al. (2026) | NBER Working Paper |
| [Difference-in-Difference Causal Forests](https://onlinelibrary.wiley.com/doi/abs/10.1002/jae.70001) | Gavrilova et al. (2025) | Journal of Applied Econometrics |
| [Machine Learning Who to Nudge](https://www.gsb.stanford.edu/faculty-research/faculty/susan-athey) | Athey, Keleher, Spiess (2025) | Journal of Econometrics |
| [Leveraging LLMs for Large-Scale Information Retrieval in Economics](https://cepr.org/voxeu/columns/leveraging-large-language-models-large-scale-information-retrieval-economics) | CEPR/VoxEU (2025) | VoxEU Column |

---

## Books

- **[Deep Learning for Economists](https://dell-research-harvard.github.io/projects/384econdl)** — Melissa Dell (Harvard). JEL 2025 + companion website with demo notebooks and knowledge base.
- **[The Means of Prediction](https://www.amazon.com/Means-Prediction-Really-Works-Benefits-ebook/dp/B0FJ2NZW7D)** — Maximilian Kasy (Oxford). How AI really works and who benefits. University of Chicago Press, Oct 2025.
- **[The Scaling Era: An Oral History of AI, 2019-2025](https://www.dwarkesh.com/podcast)** — Dwarkesh Patel & Gavin Leech. Oral history from interviews with Amodei, Hassabis, Zuckerberg.
- **[Artificial Intelligence, Learning and Computation in Economics and Finance](https://link.springer.com/book/10.1007/978-3-031-15294-8)** — Agent-based modeling with AI/ML methods. Springer, 2024.

---

## Courses and Conferences

### Courses

- [Economics of Transformative AI (EconTAI)](https://digitaleconomy.stanford.edu/etai-course/) — Stanford. Lecture slides and exercises available online.
- [The Economics of AI](https://www.coursera.org/learn/economics-of-ai) — Korinek, University of Virginia, on Coursera.
- [Data Analysis with AI v2.0](https://gabors-data-analysis.com/ai-course/) — Gabor Bekes, CEU Vienna (Jan 2026). 12-week course using LLMs for instrumental variables, DiD, simulations.
- [genaiforecon.org](https://www.genaiforecon.org/) — Korinek's companion site; updated semi-annually with tools, techniques, and use cases.
- [AI for Economists](https://sites.google.com/view/lastunen/ai-for-economists) — Jesse Lastunen's prompt-focused resource with practical templates.
- [Using AI in Research and Teaching](https://github.com/paulgp/using-ai-in-research-and-teaching) — Paul Goldsmith-Pinkham (Yale SOM).
- [Deep Learning for Dynamic Economic Models](https://github.com/sischei/Deep_Learning_For_Dynamic_Econ) — Neural networks for DSGE models (Leipzig, 2024).
- [ML & Causal Inference Short Course](https://www.gsb.stanford.edu/faculty-research/labs-initiatives/sil/research/methods/ai-machine-learning/short-course) — Susan Athey, Stanford GSB.
- [ML and Economics at Oxford](https://maxkasy.github.io/home/ML_Econ_Oxford/) — Maximilian Kasy's informal reading group.
- [EconDL](https://dell-research-harvard.github.io/projects/384econdl) — Melissa Dell's companion site with Jupyter notebooks for deep learning in economics.

### Conferences (2025-2026)

- [ESIF Economics and AI+ML Meeting](https://www.econometricsociety.org/regional-activities/schedule/2026/06/16/2026-ESIFEconomics-and-AIML-Meeting) — Econometric Society, Cornell, June 2026.
- [NBER AI and Economic Measurement](https://www.nber.org/conferences/ai-and-economic-measurement-spring-2026) — Stanford, May 2026.
- [NBER Digital Economics and AI Meeting](https://www.nber.org/conferences/digital-economics-and-ai-meeting-spring-2026) — Spring 2026.
- [IESE Economics of AI Conference](https://www.iese.edu/faculty-research/economics-ai-conference-2026/) — Barcelona, February 2026.
- [Chicago Booth: Frontiers in ML and Economics](https://www.chicagobooth.edu/research/center-for-applied-artificial-intelligence/opportunities/conference-on-frontiers-in-machine-learning-and-economics) — October 2025.

---

## Blogs, Newsletters and Community

### Newsletters and Substacks

- [genaiforecon Substack](https://genaiforecon.substack.com/) — Korinek's updates on AI tools and techniques for economists.
- [Causal Inference (Scott Cunningham)](https://causalinf.substack.com/) — AI + causal inference, Claude Code for economists, Mixtape University.
- [Autonomous Econ (Martin Wong)](https://autonomousecon.substack.com/) — How economists and financial analysts build with Claude Code and AI agents.
- [One Useful Thing (Ethan Mollick)](https://www.oneusefulthing.org/) — Wharton professor on practical AI adoption in knowledge work.
- [Platforms, AI, and BigTech (Sangeet Choudary)](https://platforms.substack.com/) — 40K+ subscribers; AI, platform strategy, ecosystem mapping.
- [Understanding AI (Timothy B. Lee)](https://www.understandingai.org) — Clear explanations of AI developments with economic framing.

### Blogs

- [Marginal Revolution](https://marginalrevolution.com/) — Tyler Cowen and Alex Tabarrok; frequent AI + economics coverage.
- [Economist Writing Every Day](https://economistwritingeveryday.com/) — AI-assisted writing workflows for economists.
- [The Rundown AI](https://www.therundown.ai/) — Daily AI newsletter.

### Podcasts

- [The Dwarkesh Podcast](https://www.dwarkesh.com/podcast) — Major interviews with AI leaders and economists (Amodei, Sutskever, Karpathy).
- [Exponential View (Azeem Azhar)](https://podcasts.apple.com/us/podcast/azeem-azhars-exponential-view/id1172218725) — AI and exponential technologies, regularly features economists.

### Key People to Follow

- **Anton Korinek** — UVA/NBER, [genaiforecon.org](https://genaiforecon.org/), TIME100 AI
- **Scott Cunningham** (@causalinf) — Baylor/Harvard, *Causal Inference: The Mixtape*, AI + econ workflows
- **Erik Brynjolfsson** (@erikbryn) — Stanford Digital Economy Lab, AI productivity J-curve
- **Antonio Mele** (@antoniomele101) — [awesome-econ-ai-stuff](https://github.com/meleantonio/awesome-econ-ai-stuff)
- **Sendhil Mullainathan** — Chicago/IMF, "Economics in the Age of Algorithms"
- **Melissa Dell** — Harvard, *Deep Learning for Economists*

---

## Institutional Resources

- [NBER — Artificial Intelligence](https://www.nber.org/topics/artificial-intelligence) — Working papers and conferences on AI and the economy.
- [NBER — Digital Economics and AI](https://www.nber.org/programs-projects/projects-and-centers/8470-digital-economics-and-artificial-intelligence-2023-2025) — Tucker & Goldfarb multi-year research program (through June 2026).
- [Stanford Digital Economy Lab](https://digitaleconomy.stanford.edu/research-area/economics-of-transformative-ai/) — Developing tools, metrics, and theories for the AI-driven economy.
- [AEI — AI Tools for Economists](https://www.aei.org/technology-and-innovation/ai-tools-for-economists-and-policy-analysts/) — Practical tool comparison for policy work.
- [OECD.AI Policy Observatory](https://oecd.ai/) — AI policy, governance, and cross-country comparisons.
- [ImpactAI — World Bank DIME](https://impactai.worldbank.org/) — AI-powered synthesis of development impact evaluations.
- [Brookings — AI and the Economy](https://www.brookings.edu/topics/artificial-intelligence/) — Labor markets, productivity, and regulation.
- [VoxDev — Generative AI for LMIC Research](https://voxdev.org/topic/technology-innovation) — AI for development economics research.
- [Oxford — Economics of the Digital and AI Economy](https://www.economics.ox.ac.uk/economics-of-the-digital-and-ai-economy) — Platforms, AI, network effects, market power.

---

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a pull request.

1. **Search existing entries** to avoid duplicates.
2. **Use the standard format:** `[Name](URL) — Brief description.`
3. **Keep descriptions concise** — one line, starting with a capital letter and ending with a period.
4. **Verify all links** are working and point to the correct resource.
5. **One pull request per addition/change** for easier review.

---

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the author has waived all copyright and related or neighboring rights to this work. See [LICENSE](LICENSE) for details.

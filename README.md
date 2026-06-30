# AI Investment Research System

An AI-powered investment research system that provides a reusable infrastructure for financial analysis and future multi-agent workflows.

## Overview

This project builds the shared infrastructure for an AI investment research platform.

It includes:

- Environment setup for Google Colab and local execution
- Secure API key management
- Financial Modeling Prep (FMP) integration
- Tavily web search integration
- Shared Pydantic data models
- Logging and output management
- Reusable tools for future AI agents

The notebook intentionally focuses on the infrastructure layer. Individual research agents are developed separately.

---

## Features

- Google Colab compatible
- Local execution support
- Automated environment validation
- Financial market data retrieval
- Web search integration
- Typed data models
- Modular architecture
- Production-ready project structure

---

## Tech Stack

- Python
- OpenAI
- Tavily API
- Financial Modeling Prep API
- Pydantic
- Requests
- Google Colab

---

## Project Structure

```
investment_research_system.ipynb

outputs/
    research/
    portfolios/
    reports/
    logs/
```

---

## Future Roadmap

Planned extensions include:

- Portfolio Constructor Agent
- Investment Research Agent
- Company Analysis Agent
- ETF Analysis Agent
- Portfolio Risk Assessment
- Report Generator
- Multi-Agent Workflow

---

## Running the Project

1. Clone the repository.
2. Add your API keys.
3. Open the notebook in Google Colab or Jupyter.
4. Execute the notebook from top to bottom.

Required API keys:

- OPENAI_API_KEY
- TAVILY_API_KEY
- FMP_API_KEY

---

## Author

Olga Guryanova

AI Project Manager | Operations & AI Automation

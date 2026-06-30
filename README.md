# AI Finance Portfolio Constructor
![Python](https://img.shields.io/badge/Python-3.11-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--5-black)
![Claude](https://img.shields.io/badge/Claude-Code-orange)
![Status](https://img.shields.io/badge/Status-Prototype-success)
An AI-powered multi-agent system that automates investment research, portfolio construction, and client proposal generation for financial advisors.

Built as a pet project to explore AI workflow design, agent orchestration, LLM-powered financial analysis, and business process automation.

---

# Business Problem

Preparing investment proposals is a time-consuming process that typically requires financial analysts to:

- Research bonds, equities, and ETFs across multiple sources
- Compare dozens of investment opportunities
- Construct portfolios based on client objectives and constraints
- Evaluate portfolio risk and expected returns
- Prepare professional investment reports and presentations

The goal of this project is to automate as much of this workflow as possible while maintaining transparency and analyst oversight.

---

# Solution

Designed a modular multi-agent workflow that automates the investment proposal process from client requirements to a presentation-ready report.

The system:

- Validates client investment mandates
- Collects market and financial data
- Researches bonds, equities, and ETFs
- Builds multiple portfolio strategies
- Reviews recommendations through an Investment Committee agent
- Generates a client-ready investment proposal
- Produces a PowerPoint presentation automatically

---

# My Contribution

I designed and implemented the solution end-to-end, including:

- Solution Architecture
- AI Workflow Design
- Multi-Agent Orchestration
- Prompt Engineering
- API Integration
- Data Modeling
- Workflow Testing & Validation
- Output Quality Assessment

---

# Workflow

```
Client Mandate
        │
        ▼
Investment Mandate Validator
        │
        ▼
Structured Mandate
        │
 ┌──────┼──────┐
 ▼      ▼      ▼
Fixed   Equity  ETF
Income  Research Research
Research
 │       │       │
 └───┬───┴───┬───┘
     ▼
Portfolio Constructor
     │
     ▼
Three Portfolio Strategies
(Conservative / Balanced / Yield)
     │
     ▼
Investment Committee Reviewer
     │
     ▼
Recommended Portfolio
     │
     ▼
Investment Proposal Generator
     │
     ▼
Presentation Generator
     │
     ▼
Client Presentation
(PPTX / PDF)
```

---

# Tech Stack

### AI & LLMs

- OpenAI GPT-5
- Claude

### Data Sources

- Financial Modeling Prep API
- Tavily Search API

### Development

- Python
- Jupyter Notebook
- Pydantic

### Output Generation

- PowerPoint Generator
- Gemini (presentation enhancement)

---

# Current Capabilities

- AI-assisted investment research
- Automated market data collection
- Portfolio construction based on investment mandates
- Multi-agent workflow orchestration
- Portfolio review workflow
- Automated investment proposal generation
- PowerPoint presentation generation

---

# Results

The current prototype successfully:

- Automates the end-to-end investment research workflow
- Evaluates 60+ investment candidates across multiple asset classes
- Generates multiple portfolio strategies aligned with client objectives
- Identifies feasibility gaps between target and realistic portfolio yields
- Produces client-ready investment proposals and presentations

---

# Key Skills Demonstrated

- AI Workflow Design
- Multi-Agent Systems
- Prompt Engineering
- Solution Architecture
- Business Process Automation
- API Integration
- Financial Data Analysis
- LLM Application Development
- Python
- AI Product Prototyping

---

# Future Improvements

Planned enhancements include:

- Retrieval-Augmented Generation (RAG)
- Portfolio backtesting
- Market sentiment analysis
- Interactive dashboard
- Multi-client support
- Performance analytics
- Cloud deployment

---

# Running the Project

1. Clone the repository.
2. Add your API keys.
3. Open the notebook in Google Colab or Jupyter Notebook.
4. Execute all notebook cells sequentially.

Required API keys:

- `OPENAI_API_KEY`
- `TAVILY_API_KEY`
- `FMP_API_KEY`

---

# Screenshots
1. Research agents outputs
<img width="2052" height="1182" alt="image" src="https://github.com/user-attachments/assets/bb51999c-6ede-4a3f-a29c-de00d561e26a" />
2. Portfolio construction results
<img width="1734" height="1592" alt="image" src="https://github.com/user-attachments/assets/e24b8717-cb76-486e-ae44-cd06f9f144bf" />
3. Investment committee review 
<img width="2000" height="1098" alt="image" src="https://github.com/user-attachments/assets/c94438f9-f719-407a-bc63-b5226f6b8e1c" />
4. Generated PowerPoint presentation
<img width="960" height="540" alt="image" src="https://github.com/user-attachments/assets/facb2038-96f7-4790-8be6-153296b94e0e" />
  <img width="960" height="540" alt="image" src="https://github.com/user-attachments/assets/6f3446be-ae83-4629-ac50-6f81453be770" />
<img width="960" height="540" alt="image" src="https://github.com/user-attachments/assets/33a2214b-502f-4d98-b9ec-2109a029422b" />
<img width="960" height="540" alt="image" src="https://github.com/user-attachments/assets/2b1822ed-8119-4b34-8ba2-b8e243eabe0e" />






---

# Project Status

🚧 Prototype / Active Development

This project is actively evolving as a playground for AI agent orchestration, financial analysis automation, and workflow design.

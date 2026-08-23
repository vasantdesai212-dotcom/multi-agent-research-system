<div align="center">

# 🧠 Multi-Agent Research System

### AI agents that research, write, and critique — together.

A collaborative pipeline of specialized LLM agents that autonomously research a topic, draft a structured answer, and critique it for quality before producing a final response.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Orchestration-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://www.langchain.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![OpenRouter](https://img.shields.io/badge/OpenRouter-LLM%20Gateway-8A2BE2?style=for-the-badge)](https://openrouter.ai/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](#-license)

</div>

---

## 📖 Overview

A **Multi-Agent Research System** is an AI-powered pipeline where multiple specialized agents work together to produce a high-quality research response — instead of relying on a single LLM to do everything.

The task is split across three stages:

- 🔍 **Research Agent** — gathers and analyzes relevant information from external sources
- ✍️ **Writer Agent** — turns that research into a structured, detailed response
- 🧐 **Critic Agent** — evaluates the draft for accuracy, relevance, completeness, and quality

The agents are chained into a **pipeline**: the output of one stage becomes the input of the next, creating a collaborative workflow that's more reliable and structured than a single-agent approach.

Built with **Python**, **LangChain**, and **OpenRouter**, this project demonstrates how multiple AI agents can be orchestrated to autonomously perform complex research tasks.

---

## 🏗️ Architecture

```mermaid
flowchart LR
    U([👤 User Query]) --> R[["🔍 Research Agent<br/>gathers & analyzes info"]]
    R --> W[["✍️ Writer Agent<br/>drafts structured response"]]
    W --> C[["🧐 Critic Agent<br/>evaluates quality & accuracy"]]
    C --> F([✅ Final Output])

    style U fill:#1C3C3C,stroke:#fff,color:#fff
    style R fill:#2563EB,stroke:#fff,color:#fff
    style W fill:#7C3AED,stroke:#fff,color:#fff
    style C fill:#DC2626,stroke:#fff,color:#fff
    style F fill:#16A34A,stroke:#fff,color:#fff
```

Each stage is handled by its own agent with a distinct role, and the pipeline (`pipeline.py`) is responsible for passing data between them in order.

---

## ✨ Features

| | |
|---|---|
| 🤖 **Multi-Agent Collaboration** | Three specialized agents, each focused on one job, instead of one overloaded prompt |
| 🔎 **Real Web Research** | Uses external research tools to pull in live, relevant information |
| 🧵 **Sequential Pipeline** | Clean hand-off of data from Research → Writer → Critic → Output |
| ✅ **Built-in Quality Check** | A dedicated Critic Agent reviews the answer before it reaches the user |
| 🌐 **OpenRouter Powered** | Swap the underlying LLM by simply changing an environment variable |
| 🖥️ **Streamlit Interface** | Simple, interactive web UI — no CLI required |

---

## 🧰 Tech Stack

- **Language:** Python
- **Orchestration:** LangChain
- **LLM Access:** OpenRouter
- **Research Tool:** Tavily API
- **Interface:** Streamlit

---

## 📁 Project Structure

```
multi-agent-research-system/
├── agents.py           # Research, Writer, and Critic agent definitions
├── pipeline.py         # Orchestrates the multi-agent workflow end-to-end
├── tools.py            # External research tools used by the agents
├── streamlit_app.py    # Streamlit front-end for the app
├── requirements.txt    # Python dependencies
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- API keys for [Tavily](https://tavily.com/) and [OpenRouter](https://openrouter.ai/)

### 1. Clone the repository

```bash
git clone https://github.com/vasantdesai212-dotcom/multi-agent-research-system.git
cd multi-agent-research-system
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
TAVILY_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here
OPENROUTER_BASE_URL=your_url_here
OPENROUTER_MODEL=model_name_here
```

| Variable | Description |
|---|---|
| `TAVILY_API_KEY` | API key used by the Research Agent to search the web |
| `OPENAI_API_KEY` | Key used to authenticate requests through the OpenAI-compatible client |
| `OPENROUTER_BASE_URL` | Base URL for the OpenRouter API endpoint |
| `OPENROUTER_MODEL` | The LLM model to route requests to via OpenRouter |

### 4. Run the app

```bash
streamlit run streamlit_app.py
```

The app will open in your browser — enter a research topic and watch the agents go to work. 🚀

---

## ⚙️ How It Works

1. **Research** — the Research Agent gathers information relevant to the query.
2. **Write** — the Writer Agent turns that research into a structured response.
3. **Critique** — the Critic Agent evaluates the response for accuracy, relevance, completeness, and quality.
4. **Deliver** — the pipeline produces the final, refined output for the user.

---

## 🗺️ Roadmap

- [ ] Add more specialized agents
- [ ] Improve critic evaluation
- [ ] Add a web interface
- [ ] Add persistent memory

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/vasantdesai212-dotcom/multi-agent-research-system/issues) or open a pull request.

---

## 📄 License

This project is licensed under the **MIT License**. Feel free to use, modify, and build on it.

---

<div align="center">

**⭐ If you found this project interesting, consider giving it a star!**

Made with 🧠 + ☕ by [Vasant Desai](https://github.com/vasantdesai212-dotcom)

</div>

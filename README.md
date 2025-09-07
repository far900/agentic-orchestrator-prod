# 🧠 Agentic Orchestrator – Production-Grade GenAI System

Built and shipped by **Farheen Fatima**, this repository showcases an end-to-end agentic system using LangGraph-style orchestration, tool/function calling, structured output validation, and evaluation/observability pipelines. Designed for real-world deployment across streaming/OTT, fintech, and LLM-native platforms.

---

## 🔧 Key Features

- **LangGraph-style orchestration** with planner/executor agents and conditional routing
- **Tool/function calling** with modular search and summarization tools
- **Structured outputs** using JSON schema validation and fallback logic
- **Hybrid retrieval** combining vector DBs and SQL-backed filters
- **Evaluation harness** tracking grounding accuracy, latency, and tool success rate
- **CI/CD integration** with GitHub Actions and Spark-based regression hooks
- **Observability** via LangSmith, Prometheus, and Grafana

---

## 🚀 Impact Highlights

- ✅ Shipped to production with 99.9% uptime across multi-agent workflows  
- 📉 Reduced agent failure rates by 40% using retries and checkpointing  
- ⚡ Accelerated release cycles by 30% via automated evaluation and CI/CD  
- 📊 Enabled real-time observability and offline eval for LLM-powered agents

---

## 🧪 Tech Stack

| Category         | Tools & Frameworks                                      |
|------------------|---------------------------------------------------------|
| Orchestration    | LangGraph, LangChain, Python                            |
| Retrieval        | FAISS, PostgreSQL, Spark                                |
| Evaluation       | LangSmith, Custom Metrics (Accuracy, Latency)           |
| CI/CD            | GitHub Actions, Jenkins                                 |
| Monitoring       | Prometheus, Grafana                                     |
| Dev Tools        | Microsoft Copilot, Claude Code, Cursor                  |

---

## 👩‍💻 Author

**Farheen Fatima**  
Senior GenAI Practitioner  
📍 Sachse, TX | Open to remote/hybrid roles in Dallas/Plano/Addison  
🔗 linkedin.com/in/fareen-fatima-s1900| 📧 soulfit900@gmail.com

---

## 📣 How to Use This Repo

1. Clone the repo and install dependencies via `requirements.txt`
2. Run `langgraph_flow.py` to execute the planner → executor → tool loop
3. Use `eval_harness.py` to evaluate agent responses with grounding accuracy and latency
4. Extend with your own tools, agents, or retrieval logic

---

## 💬 License & Contributions

Open to collaboration and feedback. Feel free to fork, extend, or reach out for joint projects in agentic orchestration or GenAI evaluation.

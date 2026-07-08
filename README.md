# 🌿 MERAKI – An English AI Agent

> *"Learn English with confidence, powered by AI."*

MERAKI is an intelligent multi-agent English learning assistant built using **Flask**, **LangGraph**, **Google Gemini**, and **LangSmith**. It routes user queries to specialized AI agents capable of assisting with **Grammar**, **Vocabulary**, **Literature**, and **Writing**, providing accurate, contextual, and educational responses.

---

## 📖 Overview

MERAKI is designed to make English learning interactive and personalized.

Instead of relying on a single prompt, MERAKI uses a **Router Agent** that understands the user's intent and delegates the request to the most suitable expert agent.

Whether you're correcting grammar, learning new vocabulary, analyzing literature, or improving your writing, MERAKI provides clear explanations while encouraging learning rather than simply giving answers.

---

## ✨ Features

- 📝 Grammar Correction & Explanation
- 📚 Vocabulary Learning
- 📖 Literature Analysis
- ✍️ Writing Assistance
- 🤖 Intelligent Query Routing using LangGraph
- ⚡ Google Gemini Integration
- 📊 LangSmith Tracing & Debugging
- 🌐 Responsive Flask Web Interface

---

# 🏗️ System Architecture

```
                    User
                      │
                      ▼
              Flask Web Interface
                      │
                      ▼
                 LangGraph Router
                      │
        ┌─────────────┼──────────────┐
        ▼             ▼              ▼
 Grammar Agent   Vocabulary Agent   Literature Agent
                      │
                      ▼
               Writing Agent
                      │
                      ▼
                 Google Gemini
                      │
                      ▼
                  AI Response
```

---

# 🧠 AI Agents

### 📝 Grammar Agent

- Grammar correction
- Sentence restructuring
- Tense correction
- Punctuation
- Grammar explanations
- Practice exercises

---

### 📚 Vocabulary Agent

- Word meanings
- Synonyms
- Antonyms
- Contextual usage
- Example sentences
- Idioms & Phrases

---

### 📖 Literature Agent

- Poetry analysis
- Novel summaries
- Character analysis
- Literary devices
- Themes & symbolism
- Shakespeare & classic literature

---

### ✍️ Writing Agent

- Essays
- Formal letters
- Informal letters
- Emails
- Reports
- Creative writing

---

# ⚙️ Tech Stack

| Category | Technology |
|-----------|------------|
| Backend | Flask |
| LLM | Google Gemini |
| Workflow | LangGraph |
| Prompt Framework | LangChain |
| Monitoring | LangSmith |
| Frontend | HTML, CSS, JavaScript |
| Language | Python |

---

# 📂 Project Structure

```
MERAKI/
│
├── agents/
│   ├── grammar_agent.py
│   ├── vocabulary_agent.py
│   ├── literature_agent.py
│   ├── writing_agent.py
│   └── router.py
│
├── graph/
│   ├── graph_builder.py
│   ├── nodes.py
│   └── state.py
│
├── prompts/
│
├── services/
│   └── gemini.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│
├── app.py
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

## Clone the repository

```bash
git clone https://github.com/your-username/MERAKI.git

cd MERAKI
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Create a `.env` file

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY

LANGSMITH_API_KEY=YOUR_LANGSMITH_API_KEY

LANGCHAIN_TRACING_V2=true

LANGCHAIN_PROJECT=MERAKI
```

---

## Run the Application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

# 💡 Example Queries

### Grammar

```
He don't likes cricket.
```

---

### Vocabulary

```
What does meticulous mean?
```

---

### Literature

```
Explain the theme of Macbeth.
```

---

### Writing

```
Write a formal leave application.
```

---

# 📊 LangGraph Workflow

```
User Query
      │
      ▼
Router Agent
      │
      ├────────► Grammar Agent
      │
      ├────────► Vocabulary Agent
      │
      ├────────► Literature Agent
      │
      └────────► Writing Agent
```

---

# 🔍 Monitoring

MERAKI integrates **LangSmith** to monitor every interaction.

Features include:

- Execution Tracing
- Prompt Inspection
- Token Usage
- Response Latency
- Error Tracking
- Workflow Visualization

---

# 🌱 Future Enhancements

- Conversation Memory
- RAG-based Knowledge Retrieval
- Speech-to-Text
- Text-to-Speech
- Multi-language Support
- PDF Analysis
- Personalized Learning Dashboard
- Quiz Generation
- Student Progress Tracking

---

# 👩‍💻 Author

**Team Asymptotes**

Built with ❤️ using Flask, LangGraph, LangChain, Google Gemini and LangSmith.

---

# ⭐ If you like this project

Give it a ⭐ on GitHub and support the project!

# 🧠 VeriSearch AI — Document-First Verified Research System (v2)

VeriSearch AI is an **offline, enterprise-style research assistant** that transforms user queries and uploaded documents into **structured, transparent, and confidence-aware research reports** using a **document-first Retrieval-Augmented Generation (RAG)** pipeline.

This version focuses on **professional research synthesis**, not chatbot-style answering.

---

## 🚩 Problem Statement

Traditional research workflows suffer from:

- Unstructured search results
- Repetitive or shallow summaries
- Mixed reliability of sources
- Lack of transparency between facts and inference

Managers and researchers need **clear, auditable, and structured reports**, not chat responses.

---

## ✅ Solution Overview

VeriSearch AI provides:

- 📄 Document-first research (PDFs, text inputs)
- 🧠 Hybrid reasoning (verified content + analytical synthesis)
- 📊 Structured, manager-ready research reports
- 🔎 Research confidence indicators
- 📄 Professional PDF export
- 💻 Fully offline execution using a local LLM

---

## 🧠 Core Concept: Hybrid Verified Mode

Instead of claiming full verification, the system **clearly separates**:

### ✔ Document-Grounded Analysis
Insights derived directly from uploaded documents

### ⚠ Analytical Reasoning
Logical synthesis based on local LLM reasoning  
*(clearly labeled — no false verification claims)*

This ensures **honesty, transparency, and enterprise trust**.

---

## 🏗️ System Architecture

User Query / Document Upload
↓
Document Extraction
↓
Chunking & Embeddings
↓
Vector Retrieval (FAISS)
↓
Local LLM Reasoning (TinyLLaMA via Ollama)
↓
Structured Research Report
↓
Confidence Scoring + PDF Export


---

## 🧰 Tech Stack

- **Python 3.11**
- **Streamlit** — UI
- **LangChain** — RAG orchestration
- **FAISS** — Vector similarity search
- **SentenceTransformers** — Local embeddings
- **Ollama** — Local LLM runtime
- **TinyLLaMA (1.1B)** — CPU-friendly LLM
- **ReportLab** — Professional PDF generation

---

## ⚙️ Installation & Setup

### 1️⃣ Install Python
Download Python 3.11  
👉 https://www.python.org/downloads/

(Enable **Add Python to PATH**)

---

### 2️⃣ Install Ollama
👉 https://ollama.com/download

Pull the model:
```bash
ollama pull tinyllama:1.1b-chat
3️⃣ Clone Repository
git clone https://github.com/Khapkeaadi24/intelligent_search_rag_24.git
cd intelligent-search-rag
4️⃣ Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate
5️⃣ Install Dependencies
pip install -r requirements.txt
6️⃣ Run Application
streamlit run app.py
Open:

http://localhost:8501
📊 Features
🔍 Research on any topic

📄 Document-based analysis

🧠 Hybrid verified reasoning

⏳ Time range configuration

🆚 Competitor analysis framework

📈 Research confidence scoring

📄 Professional PDF export

💻 Fully offline execution

📌 Use Cases
Company & market research

Technology trend analysis

Academic paper review

Strategic decision support

Internal knowledge synthesis

⚠️ Current Limitations
No live web search or URLs (by design)

Output quality depends on uploaded documents

Lightweight LLM used for local demo purposes

🔮 Planned Enhancements
Live web verification APIs

URL-level citations

Voice & image input

Multi-document cross-analysis

Docker deployment

🧾 Methodological Note
This system does not claim real-time verification in its current version.
All results are transparently labeled and generated using local AI reasoning over user-provided documents.


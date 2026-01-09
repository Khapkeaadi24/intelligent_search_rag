# 🧠 Intelligent Search-Based RAG System (Hybrid Verified Mode)

An **offline, enterprise-style research assistant** that converts open-ended user queries into **structured, transparent, and confidence-aware research reports** using a Retrieval-Augmented Generation (RAG) pipeline.

This project addresses the limitations of traditional web search such as unstructured results, repetition, and lack of verification.

---

## 🚀 Problem Statement

Traditional web search engines return large volumes of:
- unstructured information
- repetitive content
- mixed reliability sources  

Users must manually verify, compare, and structure information, which is **time-consuming and error-prone**.

---

## ✅ Solution

This project implements an **Intelligent Search-Based RAG System** that:

- Accepts **any research query**
- Retrieves **verified contextual information**
- Separates **verified facts** from **analytical inference**
- Produces **structured research reports**
- Provides a **research confidence score**
- Exports results as **PDF reports**
- Runs **fully offline** using a local LLM

---

## 🧠 Key Concept: Hybrid Verified Mode

Instead of behaving like a chatbot, the system operates in **Hybrid Verified Mode**:

- ✔ **Verified Findings**  
  Information grounded in retrieved context

- ⚠ **Analytical Inference (Not Directly Verified)**  
  Clearly labeled reasoning based on general domain knowledge

This approach balances **accuracy, transparency, and practical usefulness**, which is critical for enterprise and research use cases.

---

## 🏗️ System Architecture

User Query
↓
Verified Search Layer
↓
Text Chunking
↓
Embeddings Generation
↓
FAISS Vector Store
↓
Hybrid Verified QA (Local LLM)
↓
Structured Research Report
↓
Confidence Score + PDF Export


---

## 🧰 Tech Stack

- **Python 3.11**
- **Streamlit** – Web UI
- **LangChain** – RAG orchestration
- **FAISS** – Vector similarity search
- **SentenceTransformers** – Local embeddings
- **Ollama** – Local LLM runtime
- **TinyLLaMA (1.1B)** – Lightweight CPU-only LLM
- **ReportLab** – PDF generation

---

## ⚙️ Installation & Setup

### 1️⃣ Install Python
Install **Python 3.11.x**  
👉 https://www.python.org/downloads/

> Make sure **“Add Python to PATH”** is checked during installation.

---

### 2️⃣ Install Ollama
Download Ollama for Windows:  
👉 https://ollama.com/download

Application Preview
<img width="1916" height="904" alt="image" src="https://github.com/user-attachments/assets/2c843b83-9ab3-48ce-9cf0-4ad232e51c4c" />

After installation, pull the required model:
```bash
ollama pull tinyllama:1.1b-chat

3️⃣ Clone or Download the Project
git clone <your-repo-url>
cd intelligent-search-rag


(or download ZIP and extract)

4️⃣ Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate

5️⃣ Install Dependencies
pip install -r requirements.txt

6️⃣ Run the Application
python -m streamlit run app.py


The app will open at:

http://localhost:8501

📊 Features

🔍 Intelligent research for any query

🧠 Hybrid Verified RAG (no hidden hallucination)

⏳ Time-based filtering (6 months / 1 year)

🆚 Competitor analysis mode

🔎 Research confidence indicator

📄 PDF export (manager-ready reports)

💻 Fully offline execution

📌 Example Use Cases

Company & competitor research

Technology trend analysis

Academic or industry research

Strategic decision support

Internal knowledge exploration

⚠️ Limitations

Output quality depends on the quality of retrieved sources

Lightweight model used for low-resource environments

Real-time web citations are not enabled (architecture supports future integration)

🔮 Future Enhancements

Live web search integration (Bing / Wikipedia)

Real URL-based citations

Domain-specific research modes

Docker-based deployment


Section-level confidence visualization



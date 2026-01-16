import streamlit as st
from PIL import Image

from utils.document_loader import extract_text_from_file
from ingestion.chunker import chunk_text
from rag.embeddings import embed_chunks
from rag.vector_store import build_vector_store
from rag.qa import run_qa
from report.report_generator import generate_report
from report.pdf_exporter import export_pdf


st.set_page_config(
    page_title="VeriSearch AI",
    layout="wide"
)

# ---------- HEADER ----------
st.title("🔍 VeriSearch AI — Verified Research System")
st.caption("Document-first | Configurable | No hallucinations | API-ready")

# ---------- SIDEBAR CONFIG ----------
st.sidebar.header("🔧 Research Configuration")

research_mode = st.sidebar.selectbox(
    "Research Mode",
    ["Exploratory", "Hybrid", "Document-only"]
)

research_depth = st.sidebar.selectbox(
    "Research Depth",
    ["Summary", "Detailed", "Deep"]
)

output_style = st.sidebar.selectbox(
    "Output Style",
    ["Executive", "Technical", "Academic"]
)

time_range = st.sidebar.selectbox(
    "Time Range",
    ["Last 6 months", "Last 12 months", "All time"]
)

use_local_llm = st.sidebar.checkbox(
    "Use local AI reasoning (Ollama)",
    value=True
)

st.sidebar.markdown("---")
st.sidebar.info(
    "External APIs are intentionally disabled.\n\n"
    "This system currently performs:\n"
    "- Document-grounded synthesis\n"
    "- Honest exploratory reasoning\n\n"
    "Live verification will be added later."
)

# ---------- MAIN INPUT ----------
st.subheader("🧠 Research Input")

query = st.text_input(
    "Research Question (optional)",
    placeholder="e.g. Fintech companies in India"
)

uploaded_file = st.file_uploader(
    "Upload document (PDF or TXT)",
    type=["pdf", "txt"]
)

# ---------- VALIDATION ----------
if not query and not uploaded_file:
    st.warning("Please provide at least a research question or a document.")

# ---------- GENERATE ----------
if st.button("🚀 Generate Research Report"):
    with st.spinner("Processing research pipeline..."):

        documents = []

        if uploaded_file:
            raw_text = extract_text_from_file(uploaded_file)
            chunks = chunk_text(raw_text)
            documents = chunks

            vector_store = build_vector_store(
                embed_chunks(chunks)
            )

        answer = ""
        if query and use_local_llm:
            answer = run_qa(
                query=query,
                vector_store=vector_store if uploaded_file else None,
                mode=research_mode,
                depth=research_depth,
                style=output_style
            )

        report = generate_report(
            query=query,
            documents=documents,
            answer=answer,
            mode=research_mode,
            depth=research_depth,
            style=output_style,
            time_range=time_range
        )

        st.success("Research report generated")

        st.markdown(report)

        pdf_path = export_pdf(report)
        with open(pdf_path, "rb") as f:
            st.download_button(
                "📄 Download PDF",
                f,
                file_name="verisearch_report.pdf"
            )

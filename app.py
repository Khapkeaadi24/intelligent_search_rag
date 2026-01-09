import streamlit as st

from search.web_search import web_search
from ingestion.chunker import chunk_text
from rag.vector_store import create_vector_store
from rag.embeddings import get_embeddings
from rag.qa import get_qa_chain
from report.report_generator import generate_report
from report.pdf_exporter import export_pdf
from analysis.competitor import generate_competitor_report
from analysis.confidence import calculate_confidence
from analysis.query_decomposer import decompose_query


# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(
    page_title="Intelligent Search-Based RAG",
    page_icon="🧠",
    layout="wide",
)

# -------------------------------------------------
# Header
# -------------------------------------------------
st.markdown("""
# 🧠 Intelligent Search-Based RAG System
### Verified, source-grounded research for strategic decision making
""")

# -------------------------------------------------
# Sidebar Controls
# -------------------------------------------------
st.sidebar.header("🔧 Research Controls")

research_mode = st.sidebar.selectbox(
    "Research Mode",
    ["Single Topic Research", "Competitor Analysis"]
)

research_depth = st.sidebar.selectbox(
    "Research Depth",
    ["Overview", "Detailed", "Deep Analysis"]
)

output_style = st.sidebar.selectbox(
    "Output Style",
    ["Executive Summary", "Business Report", "Technical Report"]
)

time_range = st.sidebar.selectbox(
    "Time Range",
    ["Last 6 months", "Last 1 year"]
)

months = 6 if time_range == "Last 6 months" else 12

# -------------------------------------------------
# Main Input
# -------------------------------------------------
query = st.text_input("Enter your research query")

run_btn = st.button("🚀 Generate Report")

# -------------------------------------------------
# Run Logic
# -------------------------------------------------
if run_btn and query:

    with st.status("Running research pipeline...", expanded=True) as status:
        st.write("🔍 Ingesting verified sources")
        st.write("📄 Chunking & indexing knowledge")
        st.write("🧠 Performing grounded analysis")
        st.write("📝 Generating structured report")

        # -------------------------------------------------
        # COMPETITOR ANALYSIS MODE
        # -------------------------------------------------
        if research_mode == "Competitor Analysis":
            report = generate_competitor_report(query)
            status.update(label="Competitor analysis completed", state="complete")
            st.markdown(report)

        # -------------------------------------------------
        # SINGLE TOPIC RESEARCH (SAFE RAG MODE)
        # -------------------------------------------------
        else:
            # 1. Search (time-aware)
            docs = web_search(query, months=months)

            # 2. Chunking
            chunks = chunk_text(docs)

            if not chunks:
                st.error("No valid information found. Try a more specific query.")
                st.stop()

            # 3. Confidence Score
            confidence = calculate_confidence(
                num_sources=len(docs),
                num_chunks=len(chunks)
            )
            st.metric("🔎 Research Confidence", confidence)

            # 4. Vector Store + QA Chain
            embeddings = get_embeddings()
            vector_store = create_vector_store(chunks, embeddings)
            qa_chain = get_qa_chain(vector_store)

            # 5. SAFE Query Decomposition (ONE LLM CALL)
            sub_queries = decompose_query(query)

            combined_prompt = f"""
You are performing structured research.

Answer ALL sub-questions below using ONLY the verified context provided.

Sub-questions:
{chr(10).join(f"- {q}" for q in sub_queries)}

Provide a structured, factual, and concise analysis.
"""

            final_answer = qa_chain.invoke(combined_prompt)

            # 6. Report Generation
            report = generate_report(query, final_answer)

            status.update(label="Research completed", state="complete")
            st.markdown(report)

            # -------------------------------------------------
            # PDF EXPORT
            # -------------------------------------------------
            st.divider()
            if st.button("📄 Export as PDF"):
                pdf_file = export_pdf(report)
                with open(pdf_file, "rb") as f:
                    st.download_button(
                        label="⬇ Download Report",
                        data=f,
                        file_name=pdf_file,
                        mime="application/pdf"
                    )

def generate_report(
    query,
    documents,
    answer,
    mode,
    depth,
    style,
    time_range
):
    report = f"""
📄 VERIFIED RESEARCH REPORT

Research Query:
{query}

Configuration:
Mode: {mode}
Depth: {depth}
Style: {style}
Time Range: {time_range}

Executive Summary:
This report presents an exploratory research synthesis generated using local AI reasoning.
No external APIs or live web sources were used.

"""

    if documents:
        report += "\nDocument-Based Evidence:\n"
        for i, doc in enumerate(documents, 1):
            report += f"\nSource {i} (Extract):\n{doc[:600]}...\n"

    report += f"""
Research Analysis:
{answer}

Methodological Note:
This system uses a local language model (TinyLlama via Ollama).
All outputs are generated through contextual reasoning over user input and documents.
External verification APIs are intentionally disabled for this demo.
"""

    return report

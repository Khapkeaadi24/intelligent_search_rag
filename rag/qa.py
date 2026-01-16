from langchain_community.llms import Ollama

def run_qa(query, vector_store, mode, depth, style):
    """
    Runs structured local AI research analysis using TinyLlama via Ollama.
    """

    llm = Ollama(
        model="tinyllama:1.1b-chat",
        temperature=0.25
    )

    context = ""
    if vector_store:
        context = "\n\n".join(
            [chunk.get("text", "") for chunk in vector_store[:6]]
        )

    prompt = f"""
You are a senior research analyst.

Write a PROFESSIONAL research report using the structure below.
Do NOT include instructions, questions, or meta commentary.

========================
REPORT STRUCTURE (MANDATORY)
========================

Title:
<Clear research title>

Executive Summary:
- 1–2 concise paragraphs summarizing the topic and key insights

Research Analysis:
1. Current State
2. Key Applications
3. Challenges and Limitations
4. Future Outlook

Conclusion:
- Clear, professional conclusion

========================
RESEARCH INPUT
========================

Research Query:
{query}

Configuration:
Mode: {mode}
Depth: {depth}
Style: {style}

Document Context (if available):
{context}

========================
RULES
========================
- Write like a human analyst, not an assistant
- No placeholders
- No questions
- No mentions of APIs, web search, or model limitations
- Be neutral, factual, and structured
- If information is limited, state it analytically

BEGIN REPORT:
"""

    return llm.invoke(prompt)

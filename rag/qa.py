from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough


def get_qa_chain(vector_store):
    """
    Hybrid Verified RAG
    ULTRA-LOW RAM SAFE (TinyLLaMA)
    """

    retriever = vector_store.as_retriever(search_kwargs={"k": 2})

    prompt = PromptTemplate.from_template("""
You are an enterprise research assistant operating in HYBRID VERIFIED MODE.

Rules:
1. Use VERIFIED CONTEXT first.
2. If context is insufficient, provide clearly marked analytical inference.
3. Never mix verified facts with inference.
4. Be concise, factual, and professional.

VERIFIED CONTEXT:
{context}

QUESTION:
{question}

FORMAT:

Verified Findings:
- Facts grounded in verified context.

Analytical Inference (Not Directly Verified):
- Clearly marked insights.
""")

    llm = Ollama(
        model="tinyllama:1.1b-chat",
        temperature=0,
        num_ctx=512,
        num_gpu=0,
        num_thread=2
    )

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
    )

    return chain

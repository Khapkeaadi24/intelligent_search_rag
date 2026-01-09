from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def chunk_text(docs: list[str]):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    documents = [Document(page_content=text) for text in docs]
    chunks = splitter.split_documents(documents)
    return chunks


# report/document_processor.py

def prepare_documents(chunks):
    """
    Converts raw text chunks into numbered, readable
    document sources for report generation.
    """
    documents = []
    for idx, chunk in enumerate(chunks, start=1):
        documents.append(
            f"Source {idx}\n{chunk.strip()}"
        )
    return documents

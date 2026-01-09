def extract_text(search_results: list[str]) -> list[str]:
    """
    Convert search results into plain documents
    """
    documents = []
    for item in search_results:
        documents.append(item)
    return documents

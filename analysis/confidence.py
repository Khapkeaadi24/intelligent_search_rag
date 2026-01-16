def calculate_confidence(num_docs, num_chunks):
    return min(100, num_docs * 20 + num_chunks * 2)

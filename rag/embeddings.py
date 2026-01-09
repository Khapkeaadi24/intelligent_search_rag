from sentence_transformers import SentenceTransformer

class LocalEmbeddings:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def embed_documents(self, texts):
        return self.model.encode(texts).tolist()

    def embed_query(self, text):
        return self.model.encode([text])[0].tolist()

    # 🔥 THIS IS THE IMPORTANT PART
    def __call__(self, text):
        return self.embed_query(text)

def get_embeddings():
    return LocalEmbeddings()

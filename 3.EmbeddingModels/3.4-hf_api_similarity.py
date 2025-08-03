from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import numpy as np

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

sentences = ["Who wrote 1984?", "George Orwell wrote 1984."]

sentence_embeddings = embeddings.embed_documents(sentences)

print(f"Embedding for '{sentences[0]}': {sentence_embeddings[0][:5]}...")
print(f"Embedding for '{sentences[1]}': {sentence_embeddings[1][:5]}...")

# Compute cosine similarity using NumPy
embedding1 = np.array(embeddings.embed_query(sentences[0]))
embedding2 = np.array(embeddings.embed_query(sentences[1]))
similarity = np.dot(embedding1, embedding2) / (np.linalg.norm(embedding1) * np.linalg.norm(embedding2))
print(f"Similarity between sentences: {similarity}")
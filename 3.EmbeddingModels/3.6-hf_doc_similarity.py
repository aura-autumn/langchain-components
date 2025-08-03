from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

document=[
    "Stephen Hawking's A Brief History of Time, published in 1988, explores the fundamental questions of the universe's origin and structure in an accessible way. ",
    "The book delves into complex concepts like the Big Bang, black holes, and the nature of time, making them understandable for non-scientists. ",
    "It discusses the evolution of scientific thought from Newton to Einstein, emphasizing relativity and quantum mechanics. ",
    "Hawking also examines the possibility of a unified theory to explain all physical phenomena. ",
    " The book became a global bestseller, inspiring readers to ponder the cosmos and our place within it."
]

query="When was A Brief History of Time published?"

doc_embeddings=embedding.embed_documents(document)
query_embeddings=embedding.embed_query(query)

##Must pass 2-D lists:
score= cosine_similarity([query_embeddings], doc_embeddings)

index, score= sorted(list(enumerate(score)), key=lambda x:x[1])[-1]

print(document[index])
print(f"Similarity score is: {score}")
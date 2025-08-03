from langchain_huggingface import HuggingFaceEmbeddings

embedding=HuggingFaceEmbeddings(model='sentence-transformers/all-MiniLM-L6-v2')

text="Geroge Orwell wrote 1984."

result=embedding.embed_query(text)

print(str(result))
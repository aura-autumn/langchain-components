from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents=[
    "George Orwell wrote 1984",
    "1984 is a dystopian novel",
    "Big brother is watching you"
]

result=embedding.embed_documents(documents)

print(str(result))
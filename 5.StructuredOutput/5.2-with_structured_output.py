from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model=ChatOpenAI()

#Schema

class Review(TypedDict):
    summary: str
    sentiment: str

structured_model= model.with_structured_output(Review)

result=structured_model.invoke("5 stars. Absolutely fire!!!")

print(result)
print(result["summary"])
print(result['sentiment'])
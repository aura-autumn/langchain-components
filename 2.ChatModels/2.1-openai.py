from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model='gpt-4')

result=model.invoke("Who wrote Project Hail mary?")

print(result)
print(result.content)
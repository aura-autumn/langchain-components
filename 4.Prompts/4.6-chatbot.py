from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()
##This chatbot is with no memory or context
while True:
    user_input=input('You: ')
    if user_input=='exit':
        break
    result= model.invoke(user_input)
    print("AI:", result.content)
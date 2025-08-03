from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()

messages=[
    SystemMessage(content='You are a physics professor.'),
    HumanMessage(content='Tell me about QFT.')
]

result= model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)
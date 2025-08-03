from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

chat_template=ChatPromptTemplate([
    SystemMessage(content='You are a brilliant {domain} professor.'),
    HumanMessage(content='Explain in details- what is {topic}?')
])

prompt=chat_template.invoke({'domain':'Quantum Gravity', 'topic':'Loop Quantum Gravity'})

print(prompt)

''' Output comes out to be wrong as the dynamic placeholders are not populated in this way:
messages=[SystemMessage(content='You are a brilliant {domain} professor.', additional_kwargs={}, response_metadata={}), HumanMessage(content='Explain in details- what is {topic}?', additional_kwargs={}, response_metadata={})]
See chat_prompt_template_2 for the correct code.
'''
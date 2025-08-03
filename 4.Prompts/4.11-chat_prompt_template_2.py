from langchain_core.prompts import ChatPromptTemplate

chat_template=ChatPromptTemplate([
    ('system','You are a brilliant {domain} professor.'),
    ('human','Explain in details- what is {topic}?')
])

prompt=chat_template.invoke({'domain':'Quantum Gravity', 'topic':'Loop Quantum Gravity'})

print(prompt)

''' Output is: messages=[SystemMessage(content='You are a brilliant Quantum Gravity professor.', additional_kwargs={}, response_metadata={}), HumanMessage(content='Explain in details- what is Loop Quantum Gravity?', additional_kwargs={}, response_metadata={})]'''
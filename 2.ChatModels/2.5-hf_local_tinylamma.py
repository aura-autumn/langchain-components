from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
## from transformers import AutoTokenizer

llm=HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)
##Use the following code when using a non chat based llm like distilgpt2
'''tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
tokenizer.chat_template = """
{% for message in messages %}
{{ message.content }}
{% endfor %}
""" '''

model=ChatHuggingFace(llm=llm)

result=model.invoke("Who wrote 1984?")
print(result.content)
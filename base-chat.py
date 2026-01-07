from langchain_ollama import ChatOllama

llm = ChatOllama(
    model = "llama3",
    temperature = 0.8,
    num_predict = 256,
    # other params ...
)

messages = [
    ("system", "You are a helpful translator. Translate the user sentence to French."),
    ("human", "I love programming."),
]
aiMessage = llm.invoke(messages)

print(aiMessage)

llm2 = ChatOllama(
    model = "fredrezones55/unsloth-deepseek-r1:14b",
    temperature = 0.8,
    num_predict = 256,
    # other params ...
)

aiMessage = llm2.invoke(messages)

print(aiMessage)

llm3 = ChatOllama(
    model = "qwen2.5-coder:14b",
    temperature = 0.8,
    num_predict = 256,
    # other params ...
)
messages = [
    ("system", "You are a helpful translator. Translate the user sentence to French."),
    ("human", "I love programming."),   
]
aiMessage = llm3.invoke(messages)
print(aiMessage)
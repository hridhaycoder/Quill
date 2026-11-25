from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="gemma4:e4b",
    temperature=0,
)

while True:
    msg = input("Enter a question: ")
    response = llm.invoke(msg)
    print(response.content)
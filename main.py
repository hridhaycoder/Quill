from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="gemma4:e4b"
)

memory = []

while True:
    msg = input("Enter a question: ")
    memory.append({"role":"user","content":msg})
    response = llm.invoke(memory)
    print(response.content)
    memory.append({"role":"assistant","content":response.content})

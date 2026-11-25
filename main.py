from langchain_ollama import ChatOllama


VISION_MODEL = "qwen3-vl:4b"
SUMMARY_MODEL = "gemma4:e4b"
TEXT_MODEL = "gemma4:e4b"



transcriber = ChatOllama(
    model="qwen3-vl:4b"
)

memory = []


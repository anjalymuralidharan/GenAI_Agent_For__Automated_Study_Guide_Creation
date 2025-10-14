from langchain_ollama import OllamaEmbeddings
import chromadb

model="llama3.2:latest"
embeddings = OllamaEmbeddings(model=model)
db_client = chromadb.PersistentClient(path="./chroma_langchain_db")


from langchain_ollama import ChatOllama

llm = ChatOllama(
    model=model,
    temperature=0,
   
)
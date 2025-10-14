import config
from langchain_chroma import Chroma

def create_store(name):
    vector_store= Chroma(
    client=config.db_client,
    collection_name=name,
    embedding_function=config.embeddings,
    )
    return vector_store


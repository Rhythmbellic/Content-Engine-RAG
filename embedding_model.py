#importing libraries
from langchain_community.embeddings.ollama import OllamaEmbeddings

#embeding functions that will use for embeding both time
def get_embedding_function():
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings

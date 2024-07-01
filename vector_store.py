#importing Libraries
from langchain.vectorstores.chroma import Chroma
from document_processing import load_documents, split_documents

#path of chroma vector storage
CHROMA_PATH = "chroma"

#function to make a chroma store
def initialize_vector_store(embedding_function):
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
    return db

#function to store vectors in store
def add_documents_to_store(db, chunks):
    chunks_with_ids = calculate_chunk_ids(chunks)
    db.add_documents(chunks_with_ids)
    db.persist()

#function to calculate chunks
def calculate_chunk_ids(chunks):
    last_page_id = None
    current_chunk_index = 0

    for chunk in chunks:
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        current_page_id = f"{source}:{page}"

        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0

        chunk_id = f"{current_page_id}:{current_chunk_index}"
        last_page_id = current_page_id
        chunk.metadata["id"] = chunk_id

    return chunks

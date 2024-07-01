from langchain.document_loaders.pdf import PyPDFDirectoryLoader
from langchain.schema.document import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

DATA_PATH = r"C:\Users\rhyth\content-engine\data"

def load_documents():
    document_loader = PyPDFDirectoryLoader(DATA_PATH)
    return document_loader.load()

def split_documents(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
        length_function=len,
    )
    return text_splitter.split_documents(documents)

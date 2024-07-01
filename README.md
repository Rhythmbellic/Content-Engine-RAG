# Content-Engine-RAG


This project is a Content Engine that analyzes and compares multiple PDF documents using Retrieval Augmented Generation (RAG) techniques. It identifies and highlights the differences between documents, providing insights through a Streamlit-based chatbot interface.



Directory Structure


/content-engine
    /data
        - alphabet_10k.pdf
        - tesla_10k.pdf
        - uber_10k.pdf
    - document_processing.py
    - embedding_model.py
    - vector_store.py
    - query_engine.py
    - interface.py
    - main.py
    - requirements.txt
    - README.md


    
Files Overview


data/: Directory containing the PDF documents to be analyzed.

document_processing.py: Script for loading and splitting PDF documents.

embedding_model.py: Script to get the embedding function using Ollama.

vector_store.py: Script for initializing and managing the Chroma vector store.

query_engine.py: Script for querying the vector store and generating responses.

interface.py: Streamlit interface for user interaction.

main.py: Main script to run the Streamlit application.

requirements.txt: List of Python dependencies.

README.md: Project documentation.



Pipeline


Document Processing:

Technique: Load and split PDF documents into smaller, manageable chunks.

Libraries: langchain.document_loaders, langchain_text_splitters.

Details: Documents are loaded from the data directory and split using RecursiveCharacterTextSplitter to ensure chunks are of optimal size for embedding.


Embedding Generation:

Technique: Generate vector embeddings for document chunks using a local embedding model.

Libraries: langchain_community.embeddings.ollama.

Details: The OllamaEmbeddings model (nomic-embed-text) is used to convert document chunks into vector embeddings for semantic understanding.


Vector Store Management:

Technique: Store and manage embeddings in a vector store for efficient retrieval.

Libraries: langchain.vectorstores.chroma.

Details: The Chroma vector store is used to persistently store the embeddings. New documents are added to the store only if they do not already exist.


Query Engine:

Technique: Retrieve relevant document chunks based on user queries and generate contextual responses.

Libraries: langchain, langchain.prompts, langchain_community.llms.ollama.

Details: The query engine uses the Chroma vector store to find similar document chunks based on the user's query. A local instance of Llama2 is then used to generate responses based on the retrieved chunks.


User Interface:

Technique: Provide an interactive interface for users to input queries and receive responses.

Libraries: streamlit.

Details: A Streamlit-based interface is created to facilitate user interaction. Users can input queries, which are processed by the backend to return insights from the PDF documents.

Setup and Usage


Set up the environment:

conda create -n content-engine python=3.9
conda activate content-engine
pip install -r requirements.txt



Run the Streamlit application:
python main.py


Access the application:

Open your web browser and go to http://localhost:8501.

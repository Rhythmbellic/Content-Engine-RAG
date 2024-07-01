# Content-Engine-RAG


This project is a Content Engine that analyzes and compares multiple PDF documents using Retrieval Augmented Generation (RAG) techniques. It identifies and highlights the differences between documents, providing insights through a Streamlit-based chatbot interface.



Directory Structure


![Screenshot 2024-07-01 204822](https://github.com/Rhythmbellic/Content-Engine-RAG/assets/92723976/e7a1d4ad-a084-47d7-970d-7e22f8181e79)

    
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


![Screenshot 2024-07-01 203700](https://github.com/Rhythmbellic/Content-Engine-RAG/assets/92723976/20628707-d54c-4b1b-b3ac-d846200e0e93)



Setup and Usage


Set up the environment:

conda create -n content-engine python=3.9
conda activate content-engine
pip install -r requirements.txt



Run the Streamlit application:
python main.py


Access the application:

Open your web browser and go to http://localhost:8501.


Examples-

![Screenshot 2024-07-01 203653](https://github.com/Rhythmbellic/Content-Engine-RAG/assets/92723976/242a9eaa-9c6b-496f-aebd-6b7371d8a0c6)

![Screenshot 2024-07-01 203214](https://github.com/Rhythmbellic/Content-Engine-RAG/assets/92723976/d1980bd0-3015-42c1-82f0-e72107494423)




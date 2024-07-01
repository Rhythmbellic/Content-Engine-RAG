#importing libraries
import streamlit as st
from query_engine import query_rag

#giving the title
st.title("Content Engine - RAG")


#making functional buttons
query = st.text_input("Enter your query:")
if st.button("Submit"):
    if query:
        response = query_rag(query)
        st.write(response)

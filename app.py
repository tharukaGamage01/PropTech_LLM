import streamlit as st
import requests

st.title("PropTech LLM Chat")

# Input for user question
question = st.text_input("Ask a question about PropTech:")

if st.button("Generate Answer"):
    # Call the FastAPI backend
    response = requests.post(
        "http://127.0.0.1:8000/generate",
        json={"question": question}
    )
    if response.status_code == 200:
        st.write("**Answer:**", response.json()["response"])
    else:
        st.write("Error:", response.text)

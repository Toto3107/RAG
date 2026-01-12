import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings

def create_embeddings():
    # 1. Load the text file
    loader = TextLoader("k8s.txt")
    documents = loader.load()

    # 2. Split it into small pieces (chunks)
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    # 3. Use TinyLlama to create the "meaning" (embeddings)
    embeddings = OllamaEmbeddings(model="tinyllama")

    # 4. Save everything into a folder called 'db'
    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory="./db"
    )
    print("✅ Success! Your 'db' folder has been created with Kubernetes knowledge.")

if __name__ == "__main__":
    create_embeddings()
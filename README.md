# 🚀 NextWork RAG API (TinyLlama Edition)

A lightweight, local Retrieval-Augmented Generation (RAG) system. This API allows you to query a local knowledge base (Kubernetes documentation) using **TinyLlama** and **ChromaDB**, running entirely on your machine.



## 📂 Project Structure
```text
rag/
├── app.py           # FastAPI Server (Query Engine)
├── embed.py         # Database Creator (Ingestion)
├── k8s.txt          # Your raw knowledge base
├── requirements.txt # Python dependencies
├── .gitignore       # Git exclusion rules
└── db/              # Persistent vector store (Auto-generated)
🛠️ Tech Stack
FastAPI: High-performance web framework.

ChromaDB: Local vector database for semantic search.

Ollama: Local runner for the TinyLlama model.

Uvicorn: ASGI server for running the API.

Here is a clean, single-file README.md that you can copy and paste directly into your project. It’s written to match exactly what we've built: a direct, lightweight RAG using FastAPI, ChromaDB, and Ollama.

Markdown

# 🚀 NextWork RAG API (TinyLlama Edition)

A lightweight, local Retrieval-Augmented Generation (RAG) system. This API allows you to query a local knowledge base (Kubernetes documentation) using **TinyLlama** and **ChromaDB**, running entirely on your machine.



## 📂 Project Structure
```text
rag/
├── app.py           # FastAPI Server (Query Engine)
├── embed.py         # Database Creator (Ingestion)
├── k8s.txt          # Your raw knowledge base
├── requirements.txt # Python dependencies
├── .gitignore       # Git exclusion rules
└── db/              # Persistent vector store (Auto-generated)
🛠️ Tech Stack
FastAPI: High-performance web framework.

ChromaDB: Local vector database for semantic search.

Ollama: Local runner for the TinyLlama model.

Uvicorn: ASGI server for running the API.

⚙️ Setup Instructions
1. Prerequisites
Ollama installed and running.
TinyLlama model downloaded:
ollama pull tinyllama

2. Environment Setup
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
3. Initialize the Database
Ensure your k8s.txt file has the information you want to query, then run:
python embed.py
Note: On the first run, ChromaDB will download its embedding model (MiniLM).

🚀 Running the API
Start the server with auto-reload enabled:
uvicorn app:app --reload
🧪 How to Test
Once the server is running at http://127.0.0.1:8000:

Interactive Docs: Go to http://127.0.0.1:8000/docs to use the built-in Swagger UI.

Query via Browser: Since we use a POST or GET method, you can use the /query endpoint: http://127.0.0.1:8000/query?q=What is a Pod?

from fastapi import FastAPI
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

app = FastAPI()

# 1. Initialize the embedding model
embeddings = OllamaEmbeddings(model="tinyllama")

# 2. Connect to the saved database
vectorstore = Chroma(persist_directory="./db", embedding_function=embeddings)
retriever = vectorstore.as_retriever()

# 3. Setup TinyLlama as our "Brain"
llm = OllamaLLM(model="tinyllama")

# 4. Create a Prompt Template (Required for modern chains)
# This tells the LLM how to handle the context it finds in the database.
system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer the question. "
    "If you don't know the answer, just say that you don't know. "
    "\n\n"
    "{context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

# 5. Build the modular RAG chain
# First, create the chain that combines documents into the prompt
question_answer_chain = create_stuff_documents_chain(llm, prompt)

# Second, link the retriever to that chain
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

@app.get("/query")
async def query_ai(q: str):
    # The modern chain expects a dictionary with the key "input"
    response = rag_chain.invoke({"input": q})
    
    # The output contains the "answer", and also the "context" (source docs)
    return {
        "answer": response["answer"],
        "sources_found": len(response["context"])
    }
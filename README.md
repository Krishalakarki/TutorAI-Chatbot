# TutorAI Chatbot — RAG-based Application
## Project Overview
A college PDF tutor chatbot that helps students learn from their own study materials. Upload PDFs (lecture notes, textbooks, assignments), and the AI answers your questions by retrieving the most relevant content before generating explanations.

## 🧠 What is RAG?
Retrieval-Augmented Generation (RAG) enhances a language model by first retrieving relevant context from a knowledge base.
This improves accuracy, prevents hallucinations, and is ideal for educational content like college notes and textbooks.

## 🔄 Architecture
User uploads PDF
        ↓
PDF Loader → Text Extraction → Chunking
        ↓
Query Embedding → Pinecone Vector DB (Hugging Face embeddings)
        ↓
Relevant Content Retrieved
        ↓
RAG Chain (Groq via LangChain)
        ↓
AI-generated Answer

## 📚 Features

Upload college PDFs (notes, textbooks, assignments)

Auto-extracts text and splits into semantic chunks

Embeds chunks using Hugging Face embeddings (sentence-transformers/all-MiniLM-L6-v2)

Stores embeddings in Pinecone Vector DB 

Uses Groq (llama-3.1-8b-instant)for accurate responses

FastAPI backend with endpoints for file upload and asking questions

Streamlit frontend for interactive Q&A

## 🌐 Tech Stack
Component	   Tech Used
LLM	         Groq API (LLaMA3-70B)
Embeddings	 Hugging Face Embeddings
VectorDB   	 Pinecone
Framework	  LangChain
Backend	    FastAPI
Frontend	  Streamlit

##  API Endpoints
POST /upload_pdfs/ --- Upload one or more PDF files

POST /ask/ --- Ask a question --- Form field: `question`

## 📁 Folder Structure
TutorAI/
├── server/
│   ├── routes/
│   │   ├── __pycache__/
│   │   │   ├── ask_question.cpython-313.pyc
│   │   │   └── upload_pdfs.cpython-313.pyc
│   │   ├── ask_question.py
│   │   └── upload_pdfs.py
│   ├── modules/
│   │   ├── __pycache__/
│   │   │   ├── llm.cpython-313.pyc
│   │   │   ├── load_vectorstore.cpython-313.pyc
│   │   │   └── query_handlers.cpython-313.pyc
│   │   ├── llm.py
│   │   ├── load_vectorstore.py
│   │   ├── pdf_handlers.py
│   │   └── query_handlers.py
│   ├── middlewares/
│   │   ├── __pycache__/
│   │   │   └── exception_handlers.cpython-313.pyc
│   │   └── exception_handlers.py
│   ├── uploaded_docs/
│   │   ├── Importance of Software Quality.pdf
│   │   └── Software Quality.pdf
│   ├── logger.py
│   ├── main.py
│   ├── requirements.txt
│   └── test.py
├── client/
│   ├── __pycache__/
│   │   └── config.cpython-311.pyc
│   ├── app.py
│   ├── config.py
│   ├── requirements.txt
│   ├── components/
│   │   ├── __pycache__/
│   │   │   ├── chatUI.cpython-311.pyc
│   │   │   ├── history_download.cpython-311.pyc
│   │   │   └── upload.cpython-311.pyc
│   │   ├── chatUI.py
│   │   ├── history_download.py
│   │   └── upload.py
│   └── utils/
│       ├── __pycache__/
│       │   └── api.cpython-311.pyc
│       └── api.py
├
├── .gitignore
├── .python-version
├── main.py
└── pyproject.toml


## ⚡ Quick Setup
# Clone the repo
$ git clone https://github.com/snsupratim/medicalAssistant.git
$ cd medicalAssistant/server

# Create virtual env
$ uv venv
$ .venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
$ uv pip install -r requirements.txt

# Set environment variables (.env)
GOOGLE_API_KEY=...
GROQ_API_KEY=...
PINECONE_API_KEY=...

# Run the server
$ uvicorn main:app --reload --port 8000


$ cd medicalAssistant/client

# Create virtual env
$ uv venv
$ .venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
$ uv pip install -r requirements.txt

# Run the server
$ streamlit run app.py


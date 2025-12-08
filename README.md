# TutorAI Chatbot — RAG-based Application
## Project Overview
A college PDF tutor chatbot that helps students learn from their own study materials. Upload PDFs (lecture notes, textbooks, assignments), and the AI answers your questions by retrieving the most relevant content before generating explanations.

## 🧠 What is RAG?
Retrieval-Augmented Generation (RAG) enhances a language model by first retrieving relevant context from a knowledge base.
This improves accuracy, prevents hallucinations, and is ideal for educational content like college notes and textbooks.


---

## 🔄 Architecture
```
┌─────────────────────────────────────────────────────────────┐
│                    User uploads PDF                          │
└────────────────────────┬────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────┐
│  PDF Loader → Text Extraction → Chunking                    │
└────────────────────────┬────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────┐
│  Query Embedding → Pinecone Vector DB                        │
│  (Hugging Face embeddings)                                   │
└────────────────────────┬────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────┐
│            Relevant Content Retrieved                        │
└────────────────────────┬────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────┐
│           RAG Chain (Groq via LangChain)                     │
└────────────────────────┬────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────┐
│                 AI-generated Answer                          │
└─────────────────────────────────────────────────────────────┘
```

---

## 📚 Features

✅ Upload PDFs (notes, textbooks, assignments)

✅ Auto-extract text & split into semantic chunks

✅ Embed chunks using Hugging Face embeddings (all-MiniLM-L6-v2)

✅ Store embeddings in Pinecone Vector DB

✅ Use Groq LLaMA-3.1-8b-instant for accurate responses

✅ FastAPI backend for endpoints

✅ Streamlit frontend for interactive Q&A

## 🌐 Tech Stack

| Component      | Tech Used                                    |
|----------------|----------------------------------------------|
| 🧠 LLM        | Groq API (LLaMA3-70B)                        |
| 🔤 Embeddings | Hugging Face (all-MiniLM-L6-v2)              |
| 💾 VectorDB   | Pinecone                                     |
| 🔗 Framework  | LangChain                                    |
| ⚙️ Backend    | FastAPI                                      |
| 🖥️ Frontend   | Streamlit                                    |

---

##  API Endpoints
POST /upload_pdfs/ --- Upload one or more PDF files

POST /ask/ --- Ask a question --- Form field: `question`

## 📁 Project Structure
```
TutorAI/
├── server/                 # Backend FastAPI application
│   ├── routes/            # API endpoints
│   ├── modules/           # Core logic (LLM, vectorstore)
│   ├── middlewares/       # Error handling
│   └── main.py           # Server entry point
├── client/                # Frontend Streamlit application
│   ├── components/        # UI components
│   ├── utils/            # API client
│   └── app.py            # Client entry point
└── pyproject.toml        # Project configuration
```


## ⚡ Quick Setup
# Clone the repo
git clone https://github.com/Krishalakarki/TutorAI-Chatbot.git
cd TutorAI/server

# Create virtual env
uv venv
.venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt

# Set environment variables (.env)
GROQ_API_KEY=...

PINECONE_API_KEY=...

PINECONE_INDEX_NAME=..

## Run the server
uvicorn main:app --reload --port 8000

## Frontend Setup
cd TutorAI/client

## Create virtual env
uv venv
.venv\Scripts\activate

## Install dependencies
$ uv pip install -r requirements.txt

## Run the server
$ streamlit run app.py


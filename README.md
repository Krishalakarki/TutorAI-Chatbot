# 🎓 TutorAI Chatbot — RAG-based Application
## Project Overview
A PDF tutor chatbot that helps students learn from their own study materials. Upload PDFs (lecture notes, textbooks, assignments), and the AI answers your questions by retrieving the most relevant content before generating explanations.

##🧠 What is RAG?
Retrieval-Augmented Generation (RAG) combines retrieval of relevant information with a language model to generate accurate, context-aware answers.
It prevents hallucinations and is perfect for educational content like college notes or textbooks.

##🔄 Architecture
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

##📚 Features

Upload college PDFs (notes, textbooks, assignments)

Auto-extracts text and splits into semantic chunks

Embeds chunks using Hugging Face embeddings (sentence-transformers/all-MiniLM-L6-v2)

Stores embeddings in Pinecone Vector DB

Uses Groq (llama-3.1-8b-instant) for accurate responses

FastAPI backend with endpoints for file upload and asking questions

Streamlit frontend for interactive Q&A




Smart Assistant for Research Summarization

🚀 Overview

This is an AI-powered smart assistant that uses OpenAI's GPT model to summarize, understand, and interact with documents (PDF or TXT). Designed for research-heavy contexts like academia, legal, or technical fields, it provides:

📄 Automatic summarization (≤ 150 words)

❓ Free-form question answering

🎯 Logic-based question generation

✅ Answer evaluation with justifications

All responses are grounded in the actual document content using OpenAI's large language models (GPT-4 / GPT-3.5).

🔧 Setup Instructions

1. Clone the Repository

git clone https://github.com/Devang38/smart-assistant.git
cd smart-assistant

2. Create & Activate Virtual Environment

python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # Linux/Mac

3. Install Requirements

pip install -r requirements.txt

4. Set Your OpenAI API Key

Create a .env file in the root directory:

OPENAI_API_KEY=your-api-key-here

5. Run the App

uvicorn backend:app --reload

Visit http://127.0.0.1:8000 in your browser.

⚙️ Application Architecture

graph TD
    A[User Uploads PDF/TXT] --> B[Text Extraction (PyMuPDF or Plain Read)]
    B --> C[Auto Summary (OpenAI GPT)]
    B --> D[QA Mode / Challenge Mode]
    D --> E[Prompt Engine with Document Context]
    E --> F[OpenAI GPT Model (GPT-4)]
    F --> G[Answer/Justify/Evaluate]
    G --> H[Frontend (Streamlit/React/Gradio)]

Components:

Frontend: Built with Streamlit or React/Gradio

Backend: FastAPI-based API

Model: OpenAI GPT (via openai SDK)

Storage: In-memory context + file handling

🎯 Functional Features

1. Document Upload

Accepts .pdf and .txt files

Extracts and preprocesses text

2. Auto Summary

Summarizes document into ≤ 150 words using GPT-4

3. Ask Anything

Accepts user queries

Sends document + query to OpenAI GPT

Returns response with document-based justification

4. Challenge Me

Generates 3 logical/comprehension-based questions

Accepts user answers

Evaluates correctness + provides reference justification

💡 Bonus Features (Planned/Optional)

✅ Memory: Track previous interactions using session state

📍 Snippet Highlighting: Extract specific paragraph from text as justification

🧠 Chain-of-Thought prompting for improved logical reasoning

🧪 Sample Prompt Format

prompt = f"""
You are a document-aware research assistant. Use the following document:
{text}

Question: {question}
Answer based on the above content. Mention the paragraph or section that supports your answer.
"""

📦 Tech Stack

Frontend: Streamlit 

Backend: FastAPI

AI Model: OpenAI GPT-3.5 / GPT-4

Document Parsing: PyMuPDF, Python File I/O

Language: Python 3.10+

[Frontend: Streamlit]
   |
   ├── Upload PDF/TXT
   ├── Display Summary
   ├── Ask Anything (QA input box)
   └── Challenge Me (Generated Q&A with feedback)
       ↓
[Backend: FastAPI / LangChain]
   |
   ├── PDF/TXT Reader
   ├── Summarizer (LLM or Extractive)
   ├── Vector Indexing (FAISS / ChromaDB)
   ├── QA using Retrieved Chunks
   ├── Question Generator (LLM)
   ├── Answer Evaluator (Cosine Similarity + Keyword Match)
   └── Justification Finder (Span/Chunk Matching)


📁 Project Structure

smart-assistant/
├── app.py                # Main Streamlit app
├── backend.py            # FastAPI endpoints (QA, Challenge, Summarization)
├── document_loader.py    # PDF/TXT parsing & chunking
├── qa_logic.py           # QA, question generation & evaluation logic
├── requirements.txt
└── README.md

📌 License

This project is licensed under the MIT License.

📍 Future Enhancements

Add embeddings-based retrieval using langchain or llama-index

Enable persistent chat memory

Deploy to cloud via Render / Vercel / Streamlit Cloud

Made by Devang Yadav


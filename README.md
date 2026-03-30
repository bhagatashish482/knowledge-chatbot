# 🧠 Personal Knowledge Base Chatbot

A RAG (Retrieval Augmented Generation) chatbot that answers questions based on your PDF documents using ChromaDB vector storage and Groq's fast LLM inference.

## ✨ Features

- 📄 **PDF Document Processing** - Automatically extracts and chunks text from PDFs
- 🔍 **Semantic Search** - Uses sentence transformers for intelligent document retrieval  
- 🤖 **AI-Powered Answers** - Leverages Groq's fast LLM inference via OpenAI-compatible API
- 💬 **Interactive Web UI** - Beautiful Streamlit interface with chat history
- 📚 **Source Citations** - Shows which documents were used to generate answers

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.12
- [pipenv](https://pipenv.pypa.io/) for dependency management
- Groq API key (free at [console.groq.com](https://console.groq.com))

### 2. Installation

**Install pipenv** (if not already installed):
```bash
pip install --user pipenv
```

**Install dependencies**:
```bash
pipenv install
```

### 3. Setup

**Set up your Groq API key**:
```bash
pipenv run python setup_groq.py
```

**Process your PDF documents**:
```bash
# Add your PDF files to the data/ directory first
pipenv run python ingest.py
```

### 4. Run the App

**Start the Streamlit web interface**:
```bash
pipenv run python run_app.py
```

Or run directly:
```bash
pipenv run streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📁 Project Structure

```
knowledge-chatbot/
├── data/                   # Place your PDF files here
├── db/                     # ChromaDB vector database (auto-created)
├── app.py                  # Streamlit web interface
├── rag_chain.py           # RAG chain logic
├── ingest.py              # PDF processing and vector storage
├── chat.py                # Command-line chat interface
├── setup_groq.py          # API key setup utility
├── run_app.py             # App launcher script
├── .env                   # Environment variables (create this)
├── Pipfile                # Python dependencies
└── README.md              # This file
```

## 🔧 Configuration

### Available Models
You can change the LLM model in `rag_chain.py`:
- `llama-3.1-70b-versatile` (default - recommended)
- `mixtral-8x7b-32768` (good for longer contexts)  
- `llama2-70b-4096` (alternative option)

### Customization
- **Chunk size**: Modify `chunk_size` in `ingest.py`
- **Retrieval count**: Change `k` parameter in `rag_chain.py`
- **Temperature**: Adjust LLM creativity in `rag_chain.py`
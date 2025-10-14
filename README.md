# NoteAI

A basic Retrieval-Augmented Generation (RAG) system implementation with multi-agent support.

## 🎥 Demo Preview

Watch the demo: [NoteAI in Action](https://drive.google.com/file/d/1Unb3tkF_PyPKkCG_-QXaPRNp0WvjCiDj/view?usp=sharing)

## Prerequisites

1. Install Ollama
2. Pull the required model:
   ```bash
   ollama pull llama3.2:latest
   ```

## Setup

0. Clone the repository:
   ```bash
   git clone https://github.com/ashintv/rag_basics.git
   cd rag_basics
   ```

1. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate     # On Windows
   ```


2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Project Structure

```
rag_basics/
├── config.py              # Configuration settings
├── db.py                  # Database operations
├── loader.py              # Document loading utilities
├── main.py                # Main application entry point
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── loaded.txt             # Loaded documents tracker
├── agents/                # Multi-agent system
│   ├── __init__.py
│   ├── chat_agent.py      # Chat agent implementation
│   ├── multi_agent.py     # Multi-agent coordination
│   ├── prompt.py          # Prompt templates
│   └── __pycache__/       # Python cache files
├── chroma/                # ChromaDB storage
│   └── chroma.sqlite3
├── chroma_langchain_db/   # LangChain ChromaDB storage
│   ├── chroma.sqlite3
│   └── 9a80a6f6-fd14-4b11-95cf-13a7f7e997cf/
├── input/                 # Input documents
│   ├── hns.pdf
│   ├── small.pdf
│   └── test.pdf
├── output/                # Generated outputs
│   ├── test_medium_summary.json
│   └── test_qna.json
└── utils/                 # Utility functions
    ├── __init__.py
    ├── showdb.py          # Database visualization
    ├── write.py           # File writing utilities
    └── __pycache__/       # Python cache files
```

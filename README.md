# SimpleGenAIApp

A beginner-friendly GenAI project with two implementations:
1. **RAG Pipeline (Jupyter Notebook)**: Retrieval-Augmented Generation using LangChain, OpenAI embeddings, and FAISS vector database.
2. **Streamlit App**: Interactive web UI for Q&A with local Ollama (TinyLLAMA) model.

## What you built in this project

### 1. RAG Pipeline (`main.ipynb`)
Complete notebook pipeline for retrieval-augmented generation:
1. Load environment variables from `.env`.
2. Ingest content from the LangSmith docs page using `WebBaseLoader`.
3. Split loaded text into chunks using `RecursiveCharacterTextSplitter`.
4. Create embeddings with `OpenAIEmbeddings`.
5. Store vectors in a FAISS index.
6. Run similarity search queries on the vector store.
7. Initialize an LLM (`ChatOpenAI`, model `gpt-4o`).
8. Build a document chain with a custom prompt.
9. Build a retrieval chain that combines retriever + document chain.
10. Invoke the chain to get context-grounded answers.

### 2. Streamlit App (`main_ollama.py`)
Interactive web application using local Ollama model:
- Streamlit framework for easy UI
- Ollama TinyLLAMA model (runs locally, no API key needed)
- LangChain prompt templates and output parsing
- Real-time question answering

## Project files

- `main.ipynb`: Complete RAG notebook pipeline (ingestion, chunking, embeddings, vector store, retrieval, QA chain).
- `main_ollama.py`: Streamlit web app with local Ollama model.
- `requirements.txt`: Python dependencies.
- `README.md`: Project documentation.
- `.env`: API keys and environment configuration (local only, not committed).
- `.gitignore`: Specifies files/folders to exclude from version control (.env, .venv, __pycache__, etc).

## Tech stack

- Python 3.11
- Jupyter Notebook
- Streamlit (for web UI)
- LangChain ecosystem:
  - `langchain` (core framework)
  - `langchain-classic` (chains and legacy APIs)
  - `langchain-core` (interfaces)
  - `langchain-community` (community integrations)
  - `langchain-openai` (OpenAI integration)
  - `langchain-text-splitters` (document chunking)
- OpenAI API (for RAG notebook)
- Ollama TinyLLAMA (for streamlit app, runs locally)
- FAISS (`faiss-cpu`) (vector database)
- BeautifulSoup (`beautifulsoup4`) (web scraping)

## Setup

### Prerequisites
- Python 3.10+ (tested on 3.11)
- Ollama installed (for streamlit app): https://ollama.ai

### Installation

1. Clone the repository:
```bash
git clone https://github.com/saivarshadevoju/simple-genai-app.git
cd SimpleGenAIApp
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate     # On Windows
```

3. Install dependencies:
```bash
python -m pip install -r requirements.txt
```

4. Create a `.env` file with API keys (for RAG notebook only):
```env
OPENAI_API_KEY=your_openai_key
LANGCHAIN_API_KEY=your_langsmith_key
LANGCHAIN_PROJECT=GenAI
HF_TOKEN=your_huggingface_token
```

## Run

### Option 1: RAG Pipeline (Jupyter Notebook)
```bash
# Make sure .venv is activated
source .venv/bin/activate

# Open notebook
jupyter notebook main.ipynb
```

Then:
1. Select the correct Python kernel from `.venv`
2. Run cells from top to bottom
3. Test retrieval queries and chain invocation

### Option 2: Streamlit Web App
```bash
# Make sure .venv is activated
source .venv/bin/activate

# Make sure Ollama is running locally
# Then start the app
streamlit run main_ollama.py
```

The app will open at `http://localhost:8501`

## Notes and learnings

- **Pydantic v2 compatibility**: Ollama model requires keyword argument: `Ollama(model="tinyllama")` not `Ollama("tinyllama")`
- **LangChain imports**: For LangChain 1.x, chains APIs moved from `langchain.chains` to `langchain_classic.chains`
- **Kernel refresh**: Restart notebook kernel after changing `.env` values
- **Chunking quality**: `RecursiveCharacterTextSplitter` works better than basic character splitting for mixed-format content
- **Virtual environment**: Always activate `.venv` before running pip or streamlit commands
- **Shell issues**: Use `python -m pip` instead of direct `pip` to avoid PATH conflicts in zsh

## Next improvements

- Add multiple documentation URLs as sources
- Add `k` and search type tuning in retriever settings
- Add citation output showing which chunks were used
- Save/reload FAISS index locally for faster startup
- Deploy streamlit app to Streamlit Cloud
- Add custom styling and layout to streamlit app
- Support for additional local models (Llama 2, Mistral, etc.)


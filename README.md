# SimpleGenAIApp

A beginner-friendly GenAI project that builds a Retrieval-Augmented Generation (RAG) flow using LangChain, OpenAI embeddings, and a FAISS vector database inside a Jupyter notebook.

## What you built in this project

This project is implemented in `main.ipynb` and includes the full RAG flow:

1. Load environment variables from `.env`.
2. Ingest content from the LangSmith docs page using `WebBaseLoader`.
3. Split the loaded text into chunks using `RecursiveCharacterTextSplitter`.
4. Create embeddings with `OpenAIEmbeddings`.
5. Store vectors in a FAISS index.
6. Run similarity search queries on the vector store.
7. Initialize an LLM (`ChatOpenAI`, model `gpt-4o`).
8. Build a document chain with a custom prompt.
9. Build a retrieval chain that combines retriever + document chain.
10. Invoke the chain to get context-grounded answers.

## Project files

- `main.ipynb`: complete notebook pipeline (ingestion, chunking, embeddings, vector store, retrieval, QA chain).
- `requirements.txt`: Python dependencies.
- `.env`: API keys and environment configuration (local only, should not be committed).

## Tech stack

- Python
- Jupyter Notebook
- LangChain ecosystem (`langchain`, `langchain_classic`, `langchain_core`, `langchain_community`, `langchain_openai`)
- OpenAI API
- FAISS (`faiss-cpu`)
- BeautifulSoup (`beautifulsoup4`) for web page parsing

## Setup

1. Create and activate your Python environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file with required keys:

```env
OPENAI_API_KEY=your_openai_key
LANGCHAIN_API_KEY=your_langsmith_key
LANGCHAIN_PROJECT=GenAI
HF_TOKEN=your_huggingface_token
```

## Run

1. Open `main.ipynb` in VS Code.
2. Select the correct Python kernel.
3. Run cells from top to bottom in order.
4. Test retrieval queries and chain invocation cells.

## Notes and learnings

- For newer LangChain versions, some imports moved from `langchain.chains` to `langchain_classic.chains`.
- Restarting the notebook kernel is important after changing `.env` values.
- Better chunking improves retrieval quality; `RecursiveCharacterTextSplitter` worked better than basic character splitting for this page.

## Next improvements

- Add multiple documentation URLs as sources.
- Add `k` and search type tuning in retriever settings.
- Add citation-style output showing which chunk(s) were used.
- Save and reload FAISS index locally for faster startup.

# RAG Pipeline for APT Threat Intelligence

Standalone RAG (Retrieval-Augmented Generation) system for semantic search and question-answering over APT (Advanced Persistent Threat) intelligence reports.

## Features

- **PDF Processing**: Converts threat intelligence PDFs to searchable text chunks
- **Vector Embeddings**: GPU-accelerated semantic embeddings using HuggingFace models
- **Semantic Search**: ChromaDB vector database for fast similarity search
- **LLM-Powered Q&A**: Local LLM inference via Ollama for natural language answers
- **Metadata Extraction**: Automatic APT group and MITRE ATT&CK technique detection

## Architecture

Built with:

- **LangChain** - RAG orchestration and document processing
- **ChromaDB** - Vector database
- **HuggingFace** - Embedding model (Qwen/Qwen3-Embedding-8B)
- **Ollama** - Local LLM inference (gemma3n:e4b)
- **uv** - Fast Python package manager

## Quick Start

### 1. Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager
- [Ollama](https://ollama.ai) for LLM inference
- APT reports organized in: `data/reports/YYYY/*.pdf`

### 2. Installation

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone/navigate to project
cd rag

# Install dependencies
uv sync

# Pull Ollama model
ollama pull gemma3n:e4b
```

### 3. Configuration

```bash
# Copy environment template
cp .env.template .env

# Edit .env with your tokens
# Required: HF_TOKEN from https://huggingface.co/settings/tokens
```

### 4. Usage Pipeline

#### Step 1: Extract PDFs to Chunks

```bash
uv run tools/extract
```

Processes PDFs in `data/reports/`, creates 1000-char chunks with APT/MITRE metadata.
Output: `data/processed/chunked_documents.pkl` (~27MB for 2400 PDFs)

Options:

```bash
uv run tools/extract --max-files 10  # Test with 10 files only
```

#### Step 2: Create Embeddings

```bash
uv run tools/embed
```

Generates vector embeddings for semantic search.
Output: `data/chroma_db/` vector database

Time: 10-20 min (GPU) or 40-60 min (CPU) for full dataset

#### Step 3: Query the System

```bash
uv run tools/query "What TTPs does APT28 use?"
```

Example queries:

```bash
uv run tools/query "Which groups target financial institutions?"
uv run tools/query "What are common initial access techniques?"
uv run tools/query "Tell me about Lazarus Group's infrastructure"
```

Response includes:

- Natural language answer
- Source documents with metadata
- Confidence level
- MITRE ATT&CK techniques

## Configuration

Key settings in `src/rag/config.py`:

```python
EMBEDDING_MODEL = "Qwen/Qwen3-Embedding-8B"  # HuggingFace model
PDF_LOADER = "pymupdf4llm"                   # Markdown conversion
CHUNK_SIZE = 1000                             # Characters per chunk
CHUNK_OVERLAP = 200                           # Overlap between chunks
RETRIEVAL_K = 5                               # Documents per query
```

Override via environment variables:

```bash
export EMBEDDING_MODEL="sentence-transformers/all-MiniLM-L6-v2"
export PDF_LOADER="pdfplumber"
```

## Development

### Running Tests

```bash
# All tests
uv run pytest

# Specific test
uv run pytest tests/ingest/test_loader.py

# With coverage
uv run pytest --cov=rag --cov-report=html
```

### Adding Dependencies

```bash
# Add package
uv add package-name

# Add dev dependency
uv add --dev pytest-asyncio

# Remove package
uv remove package-name
```

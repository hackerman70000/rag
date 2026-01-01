import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


class Config:
    PROJECT_ROOT = Path(__file__).parent.parent.parent
    DATA_DIR = PROJECT_ROOT / "data"
    RAW_DATA = DATA_DIR / "raw"
    PROCESSED_DATA = DATA_DIR / "processed"
    CHROMA_DB = DATA_DIR / "chroma_db"
    REPORTS_DIR = DATA_DIR / "reports"

    COLLECTION_NAME = "apt_reports"
    EMBEDDING_MODEL = os.getenv(
        "EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2"
    )
    PDF_LOADER = os.getenv("PDF_LOADER", "pymupdf4llm")

    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200
    RETRIEVAL_K = 5

    HF_TOKEN = os.getenv("HF_TOKEN") or os.getenv("access_token")
    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

    LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
    LANGSMITH_PROJECT = os.getenv("LANGSMITH_PROJECT", "rag")
    LANGSMITH_TRACING = os.getenv("LANGSMITH_TRACING", "false")

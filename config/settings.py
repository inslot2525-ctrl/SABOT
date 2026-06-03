from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

FAISS_INDEX_PATH = "storage/faiss_index/sales.index"
METADATA_PATH = "storage/metadata/chunks.pkl"
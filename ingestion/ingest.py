import faiss
import numpy as np
import pickle
from pathlib import Path

from pypdf import PdfReader

from ingestion.chunk import chunk_text
from ingestion.embed import get_embedding

INDEX_PATH = "storage/faiss_index/sales.index"
META_PATH = "storage/metadata/chunks.pkl"

all_embeddings = []
all_metadata = []


def read_pdf(path):

    pdf = PdfReader(path)

    text = ""

    for page in pdf.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text


for pdf_file in Path("data").glob("*.pdf"):

    if pdf_file.stat().st_size == 0:
        print(f"Skipping empty file: {pdf_file.name}")
        continue

    text = read_pdf(pdf_file)

    chunks = chunk_text(text)

    for chunk in chunks:

        embedding = get_embedding(chunk)

        all_embeddings.append(embedding)

        all_metadata.append(
            {
                "text": chunk,
                "source": pdf_file.name
            }
        )

embeddings = np.array(
    all_embeddings,
    dtype=np.float32
)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

faiss.write_index(index, INDEX_PATH)

with open(META_PATH, "wb") as f:
    pickle.dump(all_metadata, f)

print("FAISS index created.")
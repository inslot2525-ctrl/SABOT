from pathlib import Path
from pypdf import PdfReader
import faiss
import numpy as np
import pickle

from ingestion.chunk import chunk_text
from ingestion.embed import get_embeddings

UPLOAD_DIR = "uploads"
INDEX_DIR = "vectorstore"


def read_pdf(pdf_path):

    text = ""

    try:

        pdf = PdfReader(pdf_path)

        for page_num, page in enumerate(pdf.pages):

            page_text = page.extract_text()

            if page_text:

                print(
                    f"\n--- PAGE {page_num + 1} ({pdf_path.name}) ---\n"
                )

                print(
                    page_text[:500]
                )

                print(
                    "\n-----------------------------------\n"
                )

                text += page_text + "\n"

    except Exception as e:

        print(
            f"Error reading {pdf_path}: {e}"
        )

    return text


def build_index():

    Path(INDEX_DIR).mkdir(
        parents=True,
        exist_ok=True
    )

    all_chunks = []
    metadata = []

    pdf_files = list(
        Path(UPLOAD_DIR).glob("*.pdf")
    )

    if len(pdf_files) == 0:

        print(
            "No PDFs found."
        )

        return

    for pdf_file in pdf_files:

        print(
            f"Processing: {pdf_file.name}"
        )

        text = read_pdf(pdf_file)
        print("\nFIRST 500 CHARS:")
        print(text[:500])
        print("\n")
        

        if not text.strip():

            print(
                f"Skipping empty file: {pdf_file.name}"
            )

            continue

        text = text.replace(
            "\n",
            " "
        )

        text = " ".join(
            text.split()
        )

        chunks = chunk_text(text)

        for chunk in chunks:

            if len(chunk.strip()) < 50:
                continue

            all_chunks.append(chunk)

            metadata.append(
                {
                    "source": pdf_file.name,
                    "text": chunk
                }
            )

    if len(all_chunks) == 0:

        print(
            "No valid chunks found."
        )

        return

    print(
        f"Total chunks: {len(all_chunks)}"
    )

    embeddings = get_embeddings(
        all_chunks
    )

    embeddings = np.array(
        embeddings,
        dtype=np.float32
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(
        dimension
    )

    index.add(
        embeddings
    )

    faiss.write_index(
        index,
        f"{INDEX_DIR}/faiss_index.bin"
    )

    with open(
        f"{INDEX_DIR}/metadata.pkl",
        "wb"
    ) as f:

        pickle.dump(
            metadata,
            f
        )

    print(
        "FAISS index created successfully."
    )


if __name__ == "__main__":

    build_index()
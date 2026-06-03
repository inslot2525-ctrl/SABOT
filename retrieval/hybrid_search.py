import faiss
import pickle
import numpy as np

from ingestion.embed import get_embedding
from config.settings import (
    FAISS_INDEX_PATH,
    METADATA_PATH
)

index = faiss.read_index(
    FAISS_INDEX_PATH
)

with open(METADATA_PATH, "rb") as f:
    metadata = pickle.load(f)


def search(query, top_k=5):

    vector = np.array(
        [get_embedding(query)],
        dtype=np.float32
    )

    distances, indices = index.search(
        vector,
        top_k
    )

    results = []

    for idx in indices[0]:

        results.append(
            metadata[idx]
        )

    return results
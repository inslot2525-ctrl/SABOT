import faiss
import pickle
import numpy as np

from ingestion.embed import get_embeddings

from config.settings import (
    FAISS_INDEX_PATH,
    METADATA_PATH
)


def load_index():

    return faiss.read_index(
        FAISS_INDEX_PATH
    )


def load_metadata():

    with open(
        METADATA_PATH,
        "rb"
    ) as f:

        return pickle.load(f)


def search(
    query,
    top_k=5
):

    index = load_index()

    metadata = load_metadata()

    query_embedding = np.array(
        [get_embeddings(query)],
        dtype=np.float32
    )

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for i, idx in enumerate(indices[0]):

        if idx < len(metadata):

            doc = metadata[idx].copy()

            doc["distance"] = float(
                distances[0][i]
            )

            results.append(doc)

    return results
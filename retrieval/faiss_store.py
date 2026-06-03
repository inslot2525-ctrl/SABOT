import faiss
import pickle
import numpy as np
import os

INDEX_PATH = "storage/faiss_index/sales.index"
METADATA_PATH = "storage/metadata/chunks.pkl"


def save_index(index):
    faiss.write_index(index, INDEX_PATH)


def load_index():
    return faiss.read_index(INDEX_PATH)


def save_metadata(metadata):

    with open(METADATA_PATH, "wb") as f:
        pickle.dump(metadata, f)


def load_metadata():

    with open(METADATA_PATH, "rb") as f:
        return pickle.load(f)
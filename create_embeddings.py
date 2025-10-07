# create_embeddings.py
import json
import numpy as np
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

CHUNKS_FILE = 'data/chunks.json'
EMB_OUT = 'data/embeddings.npz'

MODEL_NAME = 'all-MiniLM-L6-v2'

def main():
    with open(CHUNKS_FILE, 'r', encoding='utf-8') as f:
        chunks = json.load(f)
    model = SentenceTransformer(MODEL_NAME)
    embeddings = model.encode(chunks, show_progress_bar=True)
    np.savez_compressed(EMB_OUT, embeddings=embeddings, chunks=np.array(chunks, dtype=object))
    print(f"Saved embeddings to {EMB_OUT}")

if __name__ == '__main__':
    main()

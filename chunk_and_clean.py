# chunk_and_clean.py
import json
import os

IN_FILE = 'data/docs_raw.txt'
OUT_FILE = 'data/chunks.json'
MAX_WORDS = 120

def load_lines(path):
    with open(path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def chunk_paragraphs(paragraphs, max_words=MAX_WORDS):
    chunks = []
    for p in paragraphs:
        words = p.split()
        if len(words) <= max_words:
            chunks.append(p)
        else:
            i = 0
            while i < len(words):
                chunk = ' '.join(words[i:i+max_words])
                chunks.append(chunk)
                i += max_words
    return chunks

def main():
    os.makedirs('data', exist_ok=True)
    paras = load_lines(IN_FILE)
    chunks = chunk_paragraphs(paras)
    with open(OUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)
    print(f"Wrote {len(chunks)} chunks to {OUT_FILE}")

if __name__ == '__main__':
    main()

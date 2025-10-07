# app_streamlit.py
import streamlit as st
import numpy as np
from sentence_transformers import SentenceTransformer, util
import torch

EMB_FILE = 'data/embeddings.npz'
MODEL_NAME = 'all-MiniLM-L6-v2'

@st.cache_resource
def load_model():
    return SentenceTransformer(MODEL_NAME)

@st.cache_data
def load_embeddings():
    data = np.load(EMB_FILE, allow_pickle=True)
    return data['embeddings'], data['chunks']

model = load_model()
embeddings, chunks = load_embeddings()

st.title('CapillaryTech Docs — QA Chatbot (NLP)')

query = st.text_input('Ask a question about the documentation')

top_k = st.sidebar.slider('Top K results', 1, 8, 3)

if st.button('Get Answer') and query:
    q_emb = model.encode(query, convert_to_tensor=True)
    emb_tensor = torch.tensor(embeddings)
    scores = util.cos_sim(q_emb, emb_tensor)[0]
    topk = torch.topk(scores, k=top_k)

    results = []
    for score_idx, idx in zip(topk.values.tolist(), topk.indices.tolist()):
        results.append((float(score_idx), str(chunks[idx])))

    st.write('### Best matches from docs:')
    for score, txt in results:
        st.markdown(f"**Score:** {score:.4f}  \n\n {txt}")

    st.write('---')
    st.write('### Chatbot Answer (best chunk):')
    st.write(results[0][1])

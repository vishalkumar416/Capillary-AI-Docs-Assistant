# 📌 CapillaryTech Chatbot (NLP-based)

## 🔹 Project Overview  
This project is an **NLP-powered chatbot** that helps users query the **CapillaryTech Documentation**.  
Instead of manually searching through pages, users can simply ask questions, and the chatbot will return the most relevant answers from the docs.  

The chatbot works in three main steps:  
1. **Scraping** – Extracts documentation text from CapillaryTech docs site.  
2. **Processing & Embeddings** – Cleans and chunks the scraped text, then converts it into embeddings using **Sentence Transformers (all-MiniLM-L6-v2)**.  
3. **Chatbot UI** – A **Streamlit web app** where users can type queries, and the chatbot finds the closest matches from documentation based on semantic similarity.  

---

## 🔹 Features  
- ✅ **Automated scraping** of CapillaryTech docs  
- ✅ **Chunking & cleaning** of raw text for better search results  
- ✅ **Embeddings generation** using `sentence-transformers` for semantic search  
- ✅ **Similarity matching** with cosine similarity  
- ✅ **Streamlit UI** for easy interaction and demo  
- ✅ **Top-K results** slider to see multiple relevant answers  

---

## 🔹 Project Workflow  
1. **Scrape Docs**  
   - Run `scrape.py` to fetch text from documentation pages.  
   - Extracted data is saved in `data/docs_raw.txt`.  

2. **Preprocess Data**  
   - Run `chunk_and_clean.py` to split docs into smaller text chunks.  
   - Saves output in `data/chunks.json`.  

3. **Generate Embeddings**  
   - Run `create_embeddings.py` to create embeddings of all text chunks.  
   - Saves embeddings in `data/embeddings.npz`.  

4. **Run Chatbot**  
   - Run `streamlit run app_streamlit.py`  
   - Open browser at [http://localhost:8501](http://localhost:8501)  
   - Ask any question about the documentation  

---

## 🔹 Example Queries  
Try asking:  
- *“What is the Capillary loyalty program API?”*  
- *“How do I authenticate API requests?”*  
- *“Which features does CapillaryTech offer?”*  

---

## 🔹 Tech Stack  
- **Python 3.10+**  
- **Libraries**:  
  - `beautifulsoup4`, `requests` → Web scraping  
  - `sentence-transformers` → Embeddings  
  - `numpy`, `scikit-learn`, `tqdm` → Data handling  
  - `streamlit` → Web interface  

---

## 🔹 How to Run  
```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run steps
python scrape.py
python chunk_and_clean.py
python create_embeddings.py
streamlit run app_streamlit.py

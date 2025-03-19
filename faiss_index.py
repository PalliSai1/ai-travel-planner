import faiss
import json
import numpy as np
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

# Load extracted data
with open("cleaned_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    text = data["content"]

# Split text into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
documents = text_splitter.split_text(text)

# Initialize embedding model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Convert documents into embeddings
doc_embeddings = np.array([embedding_model.embed_query(doc) for doc in documents]).astype('float32')

# Create FAISS index
dimension = doc_embeddings.shape[1]  # Get embedding dimension
faiss_index = faiss.IndexFlatL2(dimension)  # L2 distance index
faiss_index.add(doc_embeddings)  # Add embeddings to index

# Save FAISS index
faiss.write_index(faiss_index, "faiss_index.index")

# Store the chunks in a JSON file
with open("faiss_documents.json", "w", encoding="utf-8") as f:
    json.dump(documents, f, indent=4, ensure_ascii=False)

print(" FAISS index created and saved successfully!")

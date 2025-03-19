import json
import numpy as np
import faiss
from langchain_huggingface import HuggingFaceEmbeddings

# Load cleaned data
with open("cleaned_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Extract content
text_data = data.get("content", "")

# Initialize embedding model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Convert text into embeddings
embedding = embedding_model.embed_query(text_data)

# Convert embedding to a NumPy array
embedding_array = np.array([embedding], dtype="float32")

# Initialize FAISS vector store
index = faiss.IndexFlatL2(embedding_array.shape[1])
index.add(embedding_array)

# Save FAISS index
faiss.write_index(index, "faiss_index.bin")

print(" Embeddings generated and stored in FAISS successfully.")

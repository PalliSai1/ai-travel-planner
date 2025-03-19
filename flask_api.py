from flask import Flask, request, jsonify
import faiss
import numpy as np
from langchain_huggingface import HuggingFaceEmbeddings
import json

app = Flask(__name__)

# Load FAISS index
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
faiss_index = faiss.read_index("faiss_index.index")

# Load chunked documents
with open("faiss_documents.json", "r", encoding="utf-8") as f:
    documents = json.load(f)

@app.route('/query', methods=['POST'])
def query_chatbot():
    try:
        user_query = request.json.get("query", "")

        # Convert user query into an embedding
        query_embedding = np.array(embedding_model.embed_query(user_query)).astype('float32').reshape(1, -1)

        # Search FAISS index for the closest match
        _, indices = faiss_index.search(query_embedding, k=3)  # Get top 3 matches

        # Retrieve the most relevant chunk(s)
        retrieved_texts = [documents[i] for i in indices[0]]

        response = {
            "query": user_query,
            "response": " ".join(retrieved_texts)  # Combine multiple responses
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=False)

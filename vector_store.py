import faiss
import pickle
from sentence_transformers import SentenceTransformer

# Load text records
with open("dataset_texts.txt", "r", encoding="utf-8") as f:
    documents = f.readlines()

# Load Sentence Transformer Model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Convert text to embeddings
embeddings = model.encode(documents, convert_to_numpy=True)

# Create FAISS index
dimension = embeddings.shape[1]
print(dimension)
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save FAISS index and documents
faiss.write_index(index, "vector_index.faiss")
with open("documents.pkl", "wb") as f:
    pickle.dump(documents, f)

print("Embeddings stored in FAISS successfully!")

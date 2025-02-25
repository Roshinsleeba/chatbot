import pandas as pd
import pickle

# Load the dataset
df = pd.read_csv("cleaned_dataset.csv")

# Check correlation
#correlation = df["Tumor Size"].corr(df["Survival Months"])
#print("Correlation between Tumor Size and Survival Months:", correlation)
#print(df["Status"])


with open("documents.pkl", "rb") as f:
    documents = pickle.load(f)
print(documents[:10])  # Print the first 10 stored documents
import faiss

index = faiss.read_index("vector_index.faiss")
print("FAISS Index Size:", index.ntotal)

import os
import faiss
import pickle
import dotenv
from sentence_transformers import SentenceTransformer
from langchain_mistralai.chat_models import ChatMistralAI

# Load API Key
dotenv.load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")

# Load FAISS Index
index = faiss.read_index("vector_index.faiss")
with open("documents.pkl", "rb") as f:
    documents = pickle.load(f)

# Load Sentence Transformer Model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize Chat Model
llm = ChatMistralAI(mistral_api_key=api_key)

def retrieve_relevant_docs(query, k=3):
    """Retrieve the top-k most relevant patient cases."""
    query_embedding = model.encode([query])
    _, indices = index.search(query_embedding, k)
    return [documents[i] for i in indices[0]]

def chatbot():
    print("Chatbot: Ask me about cancer stages, survival rates, and treatments. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Stay healthy.")
            break

        # Retrieve relevant data
        relevant_docs = retrieve_relevant_docs(user_input)

        # Use retrieved data as context for AI response
        context = "\n".join(relevant_docs)
        print("context:",context)
        response = llm.invoke(f"Use this context: {context}\n\n{user_input}")

        print(f"Chatbot: {response.content}")

if __name__ == "__main__":
    chatbot()

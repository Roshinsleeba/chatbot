import os
import dotenv
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory  # ✅ Updated import

# Load API key from .env file
dotenv.load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")

# Initialize Mistral Chat model
llm = ChatMistralAI(mistral_api_key=api_key)

# Setup memory
chat_history = ChatMessageHistory()
chat = RunnableWithMessageHistory(llm, lambda session_id: chat_history)

def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit. I will remember our conversation!")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! I hope to chat again soon.")
            break

        # Generate a response
        response = chat.invoke(user_input, config={"configurable": {"session_id": "default"}})

        print(f"Chatbot: {response.content}")

if __name__ == "__main__":
    chatbot()

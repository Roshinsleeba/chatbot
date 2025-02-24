import os
import dotenv
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.messages import HumanMessage

# Load API key from .env file
dotenv.load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")

# Initialize Mistral Chat model
llm = ChatMistralAI(mistral_api_key=api_key)

def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break

        # Generate a response
        response = llm.invoke([HumanMessage(content=user_input)])

        # Print chatbot response
        print(f"Chatbot: {response.content}")

if __name__ == "__main__":
    chatbot()

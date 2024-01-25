import openai
from utils import get_initial_message, get_chatgpt_response, update_chat
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    print("Chatbot : ChatGPT in Terminal")
    print("AI Tutor:")

    # Load API key from environment variable
    api_key = "ULWo70Y9yFF6qsE219p8LPy3"
    print(api_key)

    # Check if API key is available
    if api_key is None:
        print("Error: OPENAI_API_KEY not found in environment variables.")
        return

    openai.api_key = api_key

    model = input("Select a model (gpt-3.5-turbo or gpt-4): ")
    
    generated_messages = []
    past_queries = []
    messages = get_initial_message()

    while True:
        query = input("Query: ")

        if query.lower() == 'exit':
            break

        messages = update_chat(messages, "user", query)

        response = get_chatgpt_response(messages, model)

        messages = update_chat(messages, "assistant", response)

        past_queries.append(query)
        generated_messages.append(response)

        for i in range(len(generated_messages) - 1, -1, -1):
            print(f"User: {past_queries[i]}")
            print(f"Assistant: {generated_messages[i]}")

        print("\nShow Messages:")
        for msg in messages:
            print(f"{msg['role']}: {msg['content']}")

if __name__ == "__main__":
    main()

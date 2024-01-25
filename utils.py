import openai

def get_initial_message():
    messages = [
        {"role": "system", "content": "You are a helpful AI Tutor. Who answers brief questions about AI."},
        {"role": "user", "content": "I want to learn AI"},
        {"role": "assistant", "content": "That's awesome, what do you want to know about AI"}
    ]
    return messages

def get_chatgpt_response(messages, model="gpt-3.5-turbo", api_key=None):
    print("model: ", model)
    prompt = "\n".join([f"{msg['role']}: {msg['content']}" for msg in messages])
    api_key ="ULWo70Y9yFF6qsE219p8LPy3"
    print("ehllo",api_key)
    openai.api_key = api_key

    response = openai.completions.create(
        model=model,
        prompt=prompt,
    )

    return response['choices'][0]['text']

def update_chat(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages

import openai
#"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"
api_key = "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"
openai.api_key = api_key
print(api_key)
try:
    response = openai.completions.create(
        model="gpt-3.5-turbo",
        prompt="Hello, OpenAI!",
    )
    print("API key is valid!")
    print(response)
except Exception as e:
    print("Error: Invalid API key or other issue")
    print(e)

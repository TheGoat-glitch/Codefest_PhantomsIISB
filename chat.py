import openai

openai.api_key = "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"

def chat_with_J(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content'].strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        response = chat_with_J(user_input)
        print("Chatbot: ", response)

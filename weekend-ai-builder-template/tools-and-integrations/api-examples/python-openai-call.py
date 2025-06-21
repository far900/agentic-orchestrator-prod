import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_reply(email_text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You're a helpful assistant writing email replies."},
            {"role": "user", "content": email_text}
        ]
    )
    return response['choices'][0]['message']['content']

# Example use
if __name__ == "__main__":
    email = "Hi, can we reschedule our meeting to next week?"
    print(generate_reply(email))
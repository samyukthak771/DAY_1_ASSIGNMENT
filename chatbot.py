import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

print("Student Study Chatbot")
print("---------------------")

question = input("Ask your study question: ")

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {"role": "user", "content": question}
    ]
)

print("\nChatbot Response:")
print(response.choices[0].message.content)
import os
import json
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


# Tool: read private student data
def read_private_data():
    with open("private_data.json", "r") as file:
        return json.load(file)


print("Student AI Agent")
print("----------------")

question = input("Ask your question: ")

# Agent loop
for step in range(1, 3):

    print(f"\nAgent step {step}")

    # Step 1: use the tool
    if step == 1:
        data = read_private_data()

        print("Tool used: Reading private student data")

        # Store the tool result
        tool_result = data

    # Step 2: use the LLM with the tool result
    else:
        prompt = f"""
You are a student study assistant.

User question:
{question}

Private student data:
{json.dumps(tool_result, indent=2)}

Answer the user's question using only the relevant information
from the private student data.

Give a short and clear answer.
"""

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        answer = response.choices[0].message.content

        print("\nAgent response:")
        print(answer)

        print("\nTask completed.")
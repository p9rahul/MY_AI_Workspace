from openai import OpenAI
from dotenv import load_dotenv
import os

#load configuration from the .env file
load_dotenv()

#create a client that comminucate with ollama
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

print("=" *40)
print("     Rahul 1stAI Assistant")
print("=" *40)

while True:

    user_input = input("\nYou : ")
    if user_input.lower() == "quit":
        print("\nAI : Goodbye! Have a great day.")

    #send a question to AI model
    response = client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=[
        {
            "role":"user",
            "content":user_input
        }
    ]
    )

    #Print response
    print("\n AI Bot :", response.choices[0].message.content)

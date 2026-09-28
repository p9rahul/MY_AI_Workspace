from openai import OpenAI
from dotenv import load_dotenv
import os


'''
************* 
 1.import tools from tools.py file
 2.import tool_manager from tool_manager.py
***********
'''
# from tools import(
#     get_current_time,
#     roll_dice,
#     generate_password
# )

from tool_manager import execute_tool

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

#Create a empty list and append this list everytime.
messages =[]

while True:

    user_input = input("\nYou : ")
    
    tool_result = execute_tool(user_input)
    if tool_result:
        print("\n Python AI Bot :", tool_result)
        continue
    
   #Save & send a question in list
    messages.append(
        {
            "role":"user",
            "content":user_input
        }
    )

    if user_input.lower() == "quit":
        print("\nAI : Goodbye! Have a great day.")
        break

    response = client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages = messages
    )

    #Print response
    ai_reply =response.choices[0].message.content
    print("\n AI Bot :", ai_reply)

    #Save the AI's reply for debug purpose
    messages.append(
        {
            "role":"assistant",
            "content":ai_reply
        }
    )

    # print("\n =============Chat history Start=============")
    # #title method returns name in Upper case like- Rahul
    # for message in messages:
    #     print(f"{message['role'].title()} : {message['content']}")

    # print("\n =============Chat history End=============")

import asyncio

from openai import OpenAI
from dotenv import load_dotenv
import os

# Load configuration
load_dotenv()

# Create AI client
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

#import all function if you want to import all function -from mcp_client import*
from mcp_client import (
    connect,
    disconnect,
    discover_tools,
    execute_tool
)

# Build Tool Descriptions
def build_tool_descriptions(tools):

    descriptions = ""
    for tool in tools:
        descriptions += f"""
            Tool:
            {tool.name}

            Description:
            {tool.description}
            ----------------------------
            """
    return descriptions

#Define planner function -> Calls build_tool_descriptions so define above
def planner(user_request, tools):

    tool_descriptions = build_tool_descriptions(
        tools
    )

    ###Then create a prompt by combining user_input and Tool_Description.  and Give this prompt to Ollama. ###

    prompt = f"""
        You are an AI Planner.

        Available Tools

        {tool_descriptions}

        Instructions

        1. Select the best tool.
        2. Reply ONLY with the tool name.
        3. Do not explain.

        User Request

        {user_request}
        """
    # Above-Then Create a Prompt by combining user_input_request & tool_descriptions. Give this prompt to ollama
    response = client.chat.completions.create (
        model= os.getenv("MODEL"),
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    
    #Ollama returns the tool name
    tool_name = response.choices[0].message.content
    return tool_name.strip()
#============Planner function end============


#============Define Response function Start============
def generate_response(user_request, tool_result):

    prompt = f"""
        The user asked:

        {user_request}

        The tool returned:

        {tool_result}

        Respond directly to the user in a natural, conversational way.

        Use the tool result as the factual source.
        Transform raw tool output into a human-friendly answer.
        Do not simply copy raw values when a natural sentence would be better.
        Do not add information that is not needed to answer the request.
        Do not mention tools, internal processing, planning, or reasoning.
        Keep the response concise.
        """

    response = client.chat.completions.create (

        model=os.getenv("MODEL"),

        messages=[

            {
                "role": "user",
                "content": prompt
            }

        ]

    )

    return response.choices[0].message.content
#============Define Response function End============

#===========Main function Start===========
async def main():
    # Step 1: Connect to the MCP Client Server.
    client = await connect()

    # Step 2: Discover all available tools.
    tools = await discover_tools(
        client
    )
    print()
    print("Available Tools")
    print("----------------")

    for tool in tools:
        print(tool.name)
    print() 

    # ==========Here add code for connect ollama with MCP server==========
    ### Step 3: Planner: Take the User Input (Question). Create Tool Descriptions for each tool. Then create a prompt by combining user input and Tool Description.  and Give this prompt to Ollama. ###
    user_request = input("User : ")
    tool_name = planner(user_request,tools) #Call planner function which is define above

    print()

    print(
        "Planner Selected Tool:",
        tool_name
    )
    
    # Step 5.	Execute the selected tool. from mcp_client.py
    tool_result = await execute_tool(client, tool_name)
    # Step 6. Generate a natural language response.
    final_answer = generate_response(user_request, tool_result)  #Define this function in same file agent.py

    print()

    print(final_answer)
    # Step 6: Disconnet MCP client
    await disconnect(
        client
    )
#===========Main function End===========


#Run 
if __name__ == "__main__":
    asyncio.run(main())
    
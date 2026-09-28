'''
Rahul - import tools functions in this file and make more readable 
like when user pass time or  clock in prompt 
so it can be readable by AI/our python code assistance
'''

from tools import(
    get_current_time,
    roll_dice,
    generate_password
)

def execute_tool(user_input):
    
    text = user_input.lower()
    
    if "time" in text or "clock" in text:
        return get_current_time()
    
    if "dice" in text or "die" in text:
        return f"You rolled {roll_dice()}"
    
    if "password" in text:
        return generate_password()
    
    return None

    
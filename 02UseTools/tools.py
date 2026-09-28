#Define all functions in this file , create tools like below

from datetime import datetime

def get_current_time():
    #Function will return system date & time.
    return datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")


import random

def roll_dice():
    # Return a randon number between 1 to 6
    return random.randint(1,6)


import secrets
import string

def generate_password(length=12):
    
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password=""

    for _ in range(length):
        password += secrets.choice(characters)

    return password

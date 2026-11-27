from datetime import datetime
import random
import secrets
import string

# Getting Time 
def get_time_date():
    return datetime.now()

# print(get_time_date())

# Printing the rendom number
def roll_dic():
    return random.randint(1,6)

# def generate_password(length = 12):
#     """"Generate a secure random password """

#     characters = (
#         string.ascii_letters 
#         string.digits
#         string.punctuation
#     ) I'll check after some time not Now
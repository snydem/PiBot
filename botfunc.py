""" Helper functions to run different events that the bot should be
to complete. Just to help keep the file structure in a nice starnard
format. If you would like to add functionality to the bot I would
suggest making a function here and then adding the key word event to
the bot.py file """

import random

HELP_STRING = "Hi! I'm PiBot! I can do a variety of things, though my\
functions are limited. My general command structure looks as follows:\n\
```pibot <comand> <parameters>```\n\
If you would like a list of my commands type ```pibot help```"



def parse_content(message_content):
    parameters = message_content.split(' ')
    return parameters

def harry_sucks():
    return "based take homie"

def roll(params):
    '''Function which takes the parameters of a roll command and rolls
    the number of dice defined by the user accordingly. returns a tuple
    formatted as ([each individual roll], sum of rolls)''' 
    # get roll as a string
    roll_string = params[2:]
    
    
    dice = []    
    
    for roll in roll_string:
        if 'd' in roll and len(roll) >= 3:
            
        elif 'd' in roll and len(roll) >= 2:
    
    num = random.randint(1, bound)
    return num

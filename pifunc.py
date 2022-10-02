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
    ''' Function to parse the message content and determine the 
    parameters of a function '''
    parameters = message_content.split(' ')
    return parameters

def harry_sucks():
    # if phrase is "I miss the old harry?"

    # if phrase is "I hate harry"
    return "based take homie"


def roll(bound):
    '''Function to generate random number that emulates a dice roll'''
    num = random.randint(1, bound)
    return num

def base64Encode(string):
    ''' Function to encode a string in base64 encoding '''

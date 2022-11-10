""" Helper functions to run different events that the bot should be
to complete. Just to help keep the file structure in a nice starnard
format. If you would like to add functionality to the bot I would
suggest making a function here and then adding the key word event to
the bot.py file """

import random
import base64 as b64
 
HELP_STRING = "Hi! I'm PiBot! I can do a variety of things, though my"\
"functions are limited. My general command structure is:\n"\
"```pibot <comand> <parameters>```\n"\
"If you would like a list of my commands type ```pibot help```"

UNRECOGNIZED_FUNCTION = "Sorry, I don't recognize that function!"\
"If you think that is something that I should know how to do, please"\
"reach out to the server moderators or admins and either request a"\
"fix or new feature!"

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
            bound = int(roll[2:])
        elif 'd' in roll and len(roll) >= 2:
            bound = int(roll[1:])
        else:
            bound = int(roll)
    # roll the bound post string parsing
    num = random.randint(1, bound)
    return num

def base64(params):
    '''Function which takes a string and base64 encodes it. Useful for
    quick little string functions and silly utility I guess'''
    
    # Get the raw text
    raw_text = " ".join(params[3:])


    # encode the text
    if params[2].lower() == "encode":
        input_string = " ".join(params[3:])
        message_bytes = input_string.encode("ascii")
        base64_bytes = b64.b64encode(message_bytes)
        base64_string = base64_bytes.decode("ascii")
        return base64_string
    # decode the text
    elif params[2].lower() == "decode":
        base64_string = " ".join(params[3:])
        '''base64_bytes = base64_string.encode("ascii")
        message_bytes = b64.b64decode(base64_bytes)
        message = message_bytes.decode("ascii")'''
        message = b64.b64decode(base64_string)
        message = message.decode("ascii", "ignore")
        return message

    else:
       raise TypeError("USAGE ERROR: Pibot base64 <encode/decode> "\
               "<message>")

        
>>>>>>> 67500e3cb6ecb555ecaa51b24a847eb126c96614


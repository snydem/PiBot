""" Helper functions to run different events that the bot should be
to complete. Just to help keep the file structure in a nice starnard
format. If you would like to add functionality to the bot I would
suggest making a function here and then adding the key word event to
the bot.py file """

import random
import base64 as b64
import ast
import operator as op
from simpleeval import simple_eval

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
    the number of dice defined by the user accordingly. return message
    formatted as [each individual roll] \n sum of rolls''' 
    
    def _dice_string_parser(roll_list:list):
        '''Function created with the purpose of parsing a dice string
        into a format which is easier to work with.'''
        
        # list of operations that we will allow on dice rolls
        operators = ['+', '-']

        dice_list = []
        operations = []

        for item in roll_list:
            # e.g. "Pibot roll 1d20"
            if ('d' != item[0]) and 'd' in item and len(item) >= 3:
                dice_num = int(item[0])
                for i in range(dice_num):
                    dice_list.append(int(item[2:]))
                    if i != (dice_num - 1):
                        operations.append('+')
            
            # e.g. "Pibot roll d20"
            elif ('d' == item[0]) and 'd' in item and len(item) >= 2:
                dice_list.append(int(item[1:]))
            
            # e.g. "Pibot roll 20" or it is an operator
            elif 'd' not in item:
                if item in operators:
                    operations.append(item)
                else:
                    dice_list.append(int(item))
        
        if (len(dice_list) - len(operations)) != 1:
            raise Exception("Invalid rolls and operations combo.")
        else:
            return (dice_list, operations)

    # get roll as a string
    roll_list = params[2:]
    
    dice_list, operations_list = _dice_string_parser(roll_list)
    roll_string = ""

    for index in range(len(dice_list)):
        bound = dice_list[index]
        # roll the bound post string parsing
        num = random.randint(1, bound)
        roll_string += str(num)
        # if we are not on the last dice roll
        if index != (len(operations_list)):
            roll_string += str(operations_list[index])

    # execute the operation of the roll string
    roll_sum = simple_eval(roll_string)

    message = f"Your rolls were: {roll_string}\nTotal: {roll_sum}"
    
    return message


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

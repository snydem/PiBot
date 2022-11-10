'''
Author's Will Bond & Chris Snyder
'''
import os
import discord

# import custom botfunctions
import botfunc

from dotenv import load_dotenv


#load env vars from .env
load_dotenv()

# Define Permissions
intents = discord.Intents.default()
intents.message_content = True

# Create the client
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

# On message event handler
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith("pibot"):
        # Get the parameters from the string passed to the bot
        params = botfunc.parse_content(message.content.lower())
        
        # Get the first word to see if it contains the pibot call
        call = params[0]
        
        # if pibot is called with no function
        if len(params) == 1 and params[0] == "pibot":
            await message.channel.send(botfunc.HELP_STRING)
        
        # if pibot is called with a function
        elif len(params) > 1 and params[0] == "pibot":

            # Get the function name which was called by the bot
            func_str = params[1]
            
            # Try to get a function with that name from pifunc.py
            try:
                function = getattr(botfunc, func_str.lower())
                # pass the function the list of parameters and get the
                # result of the operation
                result = function(params)

            
            except AttributeError:
                result = "Sorry, that is not something I know how to \
                            do! If you think that is somthing that I \
                            should be able to do check your promt, and \
                            if your prompt has no errors then please \
                            inform the creators!"

            except TypeError:
                result = "Incorrect parameter passed!"

            # pass the result back as the function dictates
            await message.channel.send(result)
        
        # the parameter was not not pibot (likely a normal message)
        else:
            raw_text = message.content.lower()
             
TOKEN = os.getenv('TOKEN')

client.run(TOKEN)

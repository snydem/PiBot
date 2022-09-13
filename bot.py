'''
Author's Will Bond & Chris Snyder
'''


import os
import discord

# import custom botfunctions
import pifunc as pf

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

    if message.content.lower().startswith('pibot'):
        params = pf.parse_content(message.content.lower())

        if len(params) == 1:
            await message.channel.send(pf.HELP_STRING)

        elif params[1] == 'roll':
            if params[2].startswith('d'):
                dice = params[2]
                dice = dice.replace('d', '')
                result = pf.roll(int(dice))

                # Send the message
                await message.channel.send(f'You rolled: {result}')

            else:
                print(f'{params[2]} is not a valid roll option. Please\
                         format your parameter as:\n\
                         ```pibot roll d<number_of_sides>```')

    if message.content.lower() == "harry sucks":
        await message.channel.send(pf.harry_sucks())

TOKEN = os.getenv('TOKEN')

client.run(TOKEN)

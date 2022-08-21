import os
import discord

# Define Permissions
intents = discord.Intents.default()
intents.message_content = True

# Create the client
client = discord.Client()



@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

TOKEN = os.getenv('TOKEN');

client.run(TOKEN)

import os

import discord

# Useed for loading environment variables
import dotenv as ldenv

ldenv.load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up intents
permissions = {
    'auto_moderation': True,
    'auto_moderation_configuration': True,
    'auto_moderation_execution': True,
    'bans': True,
    'dm_messages': True,
    'dm_reactions': True,
    'dm_typing': True,
    'emojis': True,
    'emojis_and_stickers': True,
    'guild_messages': True,
    'guild_reactions': True,
    'guild_scheduled_events': True,
    'guild_typing': True,
    'guilds': True,
    'integrations': True,
    'invites': True,
    'members': True,
    'message_content': True,
    'messages': True,
    'presences': True,
    'reactions': True,
    'typing': True,
    'value': True,
    'voice_states': True,
    'webhooks': True
}
intents = discord.Intents(**permissions)

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)

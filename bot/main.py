""" 

    Hippochus - Pelochus' Python Bot
    --------------------------------
    This is a personal bot for my Discord Server!
    
"""

import os
import discord
import hippochus # Commands Library
# from dotenv import load_dotenv

# Probar a eliminar dotenv y simplemente poner los tokens y guilds directos
# NO LO SUBAS TAL CUAL A GITHUB

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

class hippochus(discord.Client):
    async def on_ready():
        for guild in client.guilds:
            if guild.name == GUILD:
                break

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

    async def on_message(message):
        if message.author == client.user:
            return

        if message.content == '$eltorito':
            response = random.choice(brooklyn_99_quotes)
            await message.channel.send(response)

client = hippochus()
client.run(TOKEN)
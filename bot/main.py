""" 

    Hippochus - Pelochus' Python Bot
    --------------------------------
    This is a personal bot for my Discord Server!
    
"""

import os
import discord
# import hippochus # Commands Library
# from dotenv import load_dotenv

# Probar a eliminar dotenv y simplemente poner los tokens y guilds directos
# NO LO SUBAS TAL CUAL A GITHUB

# load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD = os.getenv('DISCORD_GUILD')

class hippochus(discord.Client):
    async def on_ready(self):
        print('Logged in as:')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # We do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('$hinojosa'):
            await message.reply('Hello!', mention_author=True)
        elif message.content.startswith('$torito')
            await 


client = hippochus()
client.run(TOKEN)
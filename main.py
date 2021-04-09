import os
import discord
from dotenv import load_dotenv

load_dotenv()


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.content[0] == '!':
            args = message.content.split()
            if args[0] == '!status':
                await message.reply('I\'m more alive than you, fag')
            elif args[0] == '!purge':
                await message.channel.purge(limit=int(args[1]))


client = MyClient()
client.run(os.getenv('DISCORD_AUTH_TOKEN'))

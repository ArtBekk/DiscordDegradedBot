import os
import discord

from dotenv import load_dotenv
import discord_slash


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))


client = MyClient()
slashCommandHandler = discord_slash.SlashCommand(client, sync_commands=True)


@slashCommandHandler.slash(name="status",
                           description="Is this bot alive or nah")
async def status(ctx):
    await ctx.send(content="I'm more alive than you, fag")


load_dotenv()
client.run(os.getenv('DISCORD_AUTH_TOKEN'))

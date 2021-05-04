import os
import threading

import discord
import discord.ext
import discord_slash
from discord_slash.utils.manage_commands import create_option
from dotenv import load_dotenv

import utils
from priceChecker import thread_entry


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        thread = threading.Thread(target=thread_entry, args=(self,))
        thread.start()


client = MyClient()
slashCommandHandler = discord_slash.SlashCommand(client, sync_commands=True)


@slashCommandHandler.slash(name="status",
                           description="Is this bot alive or nah")
async def status(ctx):
    await ctx.send(content="I'm more alive than you, fag")


# add some kind of exception handling later
@slashCommandHandler.slash(name="purge",
                           description="When you don't want any witnesses",
                           options=[
                               create_option(
                                   name="messageNum",
                                   description="How much garbage should I remove?",
                                   option_type=4,
                                   required=True
                               )
                           ]
                           )
@discord.ext.commands.has_permissions(manage_messages=True)
async def purge(ctx, messageNum: int):
    await client.get_channel(ctx.channel_id).purge(limit=messageNum)
    await ctx.send(content="They say history is written by the winners but you're clearly a loser, whatevs")


@slashCommandHandler.slash(name="stonks_check",
                           description="Checks the prices for beef Doshirak",
                           options=[
                               create_option(
                                   name="market_place",
                                   description=r"Select shop you want to get your prices from",
                                   option_type=3,
                                   required=True
                               )
                           ])
async def stonks_check(ctx, market_place: str):
    response = utils.get_price(utils.links_map.get(market_place, None)).get("message")
    await ctx.send(content=response)


load_dotenv()
client.run(os.getenv('DISCORD_AUTH_TOKEN'))

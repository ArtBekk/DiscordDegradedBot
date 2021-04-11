import os
from dotenv import load_dotenv

import discord
from discord.ext.commands import has_permissions, CheckFailure

import discord_slash
from discord_slash.utils.manage_commands import create_option

from bs4 import BeautifulSoup
import urllib.request


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))


client = MyClient()
slashCommandHandler = discord_slash.SlashCommand(client, sync_commands=True)


@slashCommandHandler.slash(name="status",
                           description="Is this bot alive or nah")
async def status(ctx):
    await ctx.send(content="I'm more alive than you, fag")


"""@slashCommandHandler.slash(name="purge",
                           description="When you don't want any witnesses",
                           options=[
                               create_option(
                                   name="messageNum",
                                   description="How much garbage shall I remove?",
                                   option_type=4,
                                   required=True
                               )
                           ]
                           )
async def status(ctx, messageNum: int):
    await ctx.message.channel.purge(limit=messageNum)"""


@slashCommandHandler.slash(name="stonks_check",
                           description="Checks the prices for beef Doshirak")
async def stonks_check(ctx):
    sample = urllib.request.urlopen(
        "https://lenta.com/product/lapsha-bystrogo-prigotovleniya-doshirak-so-vk-govyadiny-rossiya-105g-245818/")
    my_bytes = sample.read()
    my_str = my_bytes.decode("utf8")
    sample.close()
    soup = BeautifulSoup(my_str, 'html.parser')
    regular_price = soup.find('div', {"class": "sku-price sku-price--primary sku-prices-block__price"}).text.split()
    card_price = soup.find('div', {"class": "sku-price sku-price--primary sku-prices-block__price"}).text.split()
    regular_price = f"{regular_price[0]},{regular_price[1]}{regular_price[2]}"
    card_price = f"{card_price[0]},{card_price[1]}{card_price[2]}"
    await ctx.send(
        content=f"Price for bums w/o the card: {regular_price} and price for kings with the card: {card_price}")


load_dotenv()
client.run(os.getenv('DISCORD_AUTH_TOKEN'))

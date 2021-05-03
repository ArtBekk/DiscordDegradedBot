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


@slashCommandHandler.slash(name="purge",
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
async def purge(ctx, messageNum: int):
    await client.get_channel(ctx.channel_id).purge(limit=messageNum)
    await ctx.send(content="Succass")


@slashCommandHandler.slash(name="stonks_check",
                           description="Checks the prices for beef Doshirak",
                           options=[
                               create_option(
                                   name="market_place",
                                   description=r"Select shop you want to get your prices from where",
                                   option_type=3,
                                   required=True
                               )
                           ])
async def stonks_check(ctx, market_place: str):
    response = get_price(links_map.get(market_place, None))
    await ctx.send(
        content=response)


links_map = {
    "metro": "https://kemerovo.metro-cc.ru/category/bakaleya/produkty-bystrogo-prigotovleniya/lapsha-govyadina-doshirak-90g-488492",
    "lenta": "https://lenta.com/product/lapsha-bystrogo-prigotovleniya-doshirak-so-vk-govyadiny-rossiya-90g-051625/"}


def get_price(url: str):
    if "lenta" in url:
        return lenta_get_price(url)
    elif "metro" in url:
        return metro_get_price(url)


def lenta_get_price(url: str):
    sample = urllib.request.urlopen(url)
    my_bytes = sample.read()
    my_str = my_bytes.decode("utf8")
    sample.close()
    soup = BeautifulSoup(my_str, 'html.parser')
    regular_price = soup.find('div', {"class": "sku-price sku-price--regular sku-prices-block__price"}).text.split()
    card_price = soup.find('div', {"class": "sku-price sku-price--primary sku-prices-block__price"}).text.split()
    regular_price = f"{regular_price[0]},{regular_price[1]}{regular_price[2]}"
    card_price = f"{card_price[0]},{card_price[1]}{card_price[2]}"
    return f"Beef dooshirak's price in Lenta for bums w/o the card: {regular_price} and price for kings with the card: {card_price}"


def metro_get_price(url: str):
    sample = urllib.request.urlopen(url)
    my_bytes = sample.read()
    my_str = my_bytes.decode("utf8")
    sample.close()
    soup = BeautifulSoup(my_str, 'html.parser')
    price = "".join(soup.find('span', {"itemprop": "price"}).text.split())
    return f"Beef dooshirak's price in metro {price} в деревянных"


load_dotenv()
client.run(os.getenv('DISCORD_AUTH_TOKEN'))

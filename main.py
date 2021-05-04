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

    async def on_message(self, message):
        if message.content == 'hehe':
            await message.channel.send('https://media.giphy.com/media/dPEJxh06y4OTC/giphy.gif')
        if message.content == 'noice':
            await message.channel.send('https://media.giphy.com/media/yJFeycRK2DB4c/giphy.gif')
        if message.content == 'пиздец':
            await message.channel.send('https://media.giphy.com/media/Zqe1S3qNQxsuQ/giphy.gif')
        if message.content == 'wiggle':
            await message.channel.send('https://media.giphy.com/media/b3Gp6a25caNZC/giphy.gif')
        if message.content == 'smugwink':
            await message.channel.send('https://media.giphy.com/media/wkW0maGDN1eSc/giphy.gif')
        if message.content == 'kawaii':
            await message.channel.send('https://media.giphy.com/media/anDhBXwgvIa7m/giphy.gif')
            await message.channel.send("Fucking weebs")
        if message.content == 'eh?':
            await message.channel.send('https://media.giphy.com/media/3o7btMCltyDvSgF92E/giphy.gif')
        if message.content == 'владыка' or message.content == 'overlord':
            await message.channel.send('https://media.giphy.com/media/Mfq2ko7m1eMaQ/giphy.gif')
        if message.content == 'derpmeow':
            await message.channel.send('https://tenor.com/view/cat-meow-big-lips-gif-13233291')
            await message.channel.send('Internet was a mistake')
        if message.content == 'mememe':
            await message.channel.send('https://media.giphy.com/media/YZX4FWwOJTK5W/giphy.gif')
        if message.content == 'че бля' or message.content == 'чебля' or message.content == 'чё бля' or message.content == 'чёбля':
            await message.channel.send('https://tenor.com/view/buff-pikachu-strong-muscle-pokemon-gif-15308559')
            await message.channel.send('ESKETIT (╯°□°）╯︵ ┻━┻')
        if message.content == 'насука' or message.content == 'на сука':
            await message.channel.send('https://tenor.com/view/anime-gif-9509158')
            await message.channel.send('HIT HIM IN THE FACE')
        if message.content == 'ня' or message.content == 'nya':
            await message.channel.send('https://tenor.com/view/anime-cat-cute-gif-16038419')
            await message.channel.send('I feel sad about my job')
        if message.content == 'дя':
            await message.channel.send('https://tenor.com/view/anime-sparkle-happy-gif-6014346')
        if message.content == 'бля':
            await message.channel.send('https://tenor.com/view/blends-anime-maika-gif-10176024')
            await message.channel.send("Someone's fucked up and I'm sure as hell it ain't me")
        if message.content == 'nom' or message.content == 'жрать':
            await message.channel.send('https://tenor.com/view/eat-crab-anime-loli-dragon-gif-9920851')
        if message.content == 'батя':
            await message.channel.send('https://tenor.com/view/norogami-anime-slide-gif-4697082')


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

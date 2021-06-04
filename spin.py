# BOT TESTING SERVER LINK:
# https://discord.gg/UEwf6RWqU2
# Created by: Mizu (M1zushi)

# PACKAGES & IMPORTS
import discord

import random
from discord.ext import commands

import os
from dotenv import load_dotenv
load_dotenv('.env')

# SETS UP BASICS
client = commands.Bot(command_prefix = "ps.",
                      case_insensitive = True,
                      activity = discord.Activity(type=discord.ActivityType.playing, name='sls spam'),
                      status = discord.Status.dnd
                      )
client.remove_command('help')

@client.event
async def on_ready():
    print('Time to spam sls.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pen is spinning {round(client.latency * 1000)}ms late.')

@client.command()
async def drop(ctx):
    if ctx.author.id in {int(os.getenv('MIZU_ID'))}:
        await ctx.send('I dropped my mod...')
        await client.logout()


# HELP COMMAND: GIVES INFO ABOUT USING THE BOT
# @client.command()
# async def help(ctx):
#     pass


# ATTACHES POSTS ABOUT LEARNING ORDER
@client.command()
async def trickorder(ctx):
    await ctx.send(file=discord.File('pics/megatrickorder.png'))

@client.command()
async def isuktrickorder(ctx):
    await ctx.send('http://isukps.blogspot.com/2017/01/power-trick-learning-and-difficulty.html')


# INVITES TO DISCORD PS SERVERS
@client.command()
async def discord_workshop(ctx):
    await ctx.send('https://discord.gg/aCtV5ZAu9X')

@client.command()
async def discord_reddit(ctx):
    await ctx.send('https://discord.gg/9bVNK8mefb')

@client.command()
async def discord_penstock(ctx):
    await ctx.send('https://discord.gg/BxfewGYbQM')

@client.command()
async def discord_penmodding(ctx):
    await ctx.send('https://discord.gg/vXVWZz6UCv')

@client.command()
async def discord_mango(ctx):
    await ctx.send('https://discord.gg/Hrg6FHf')

@client.command()
async def discord_fenspinner(ctx):
    await ctx.send('https://discord.gg/M2qyDhc8Hr')

@client.command()
async def discord_frenchboard(ctx):
    await ctx.send('https://discord.gg/zSWBsd4c3b')

@client.command()
async def discord_thaispinner(ctx):
    await ctx.send('https://discord.gg/QjGZh2t')

@client.command()
async def discord_polishboard(ctx):
    await ctx.send('https://discord.gg/MCXEnkh')

@client.command()
async def discord_germancommunity(ctx):
    await ctx.send('https://discord.com/invite/aUuz8sh')


# ATTACHES LINKS FOR PS LINKAGES
@client.command()
async def breakdowngenerator(ctx):
    await ctx.send('https://limezzje.github.io/PS/')

# @client.command()
# async def sls(ctx):
#     await ctx.send('Literally all blocked cmon Tigres repost')


# ATTACHES LINKS FOR POPULAR CVS/SOLOS/PROMOS
# @client.command()
# async def controversial_cv(ctx):
#     await ctx.send('idfk')


# RUNS BOT
client.run(os.getenv('DISCORD_TOKEN'))

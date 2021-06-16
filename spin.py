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
client = commands.Bot(command_prefix = 'ps ',
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
    await ctx.send('https://discord.gg/U3CpbYY3fP')

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

@client.command()
async def discord_birthdaycrimes(ctx):
    await ctx.send('https://discord.gg/mYkh4nu9Uv')


# ATTACHES EXPLANATION FOR PS NOTATIONS
@client.command()
async def notation(ctx):
    await ctx.send('''```

    ```''')


# ATTACHES LINKS FOR PS LINKAGES
@client.command()
async def breakdowngenerator(ctx):
    await ctx.send('https://limezzje.github.io/PS/')

@client.command()
async def sls(ctx):
    await ctx.send('Playlist: https://youtube.com/playlist?list=PLqvo4PPYx7nU8j3Cjz2u6dZ7s0FERNJ7y')

@client.command()
async def sls1(ctx):
    await ctx.send('SLS 1: https://youtu.be/a7AoLeswfuU')

@client.command()
async def sls2(ctx):
    await ctx.send('SLS 2: https://youtu.be/S0XiczC333A')

@client.command()
async def sls3(ctx):
    await ctx.send('SLS 3: https://youtu.be/7sSxBwdLsz0')

@client.command()
async def sls4(ctx):
    await ctx.send('SLS 4: https://youtu.be/JAnskN6yrI4')

@client.command()
async def sls5(ctx):
    await ctx.send('SLS 5: https://youtu.be/sTGL8CwVmUU')

@client.command()
async def sls6(ctx):
    await ctx.send('SLS 6: https://youtu.be/O0pGMTkd1X8')

@client.command()
async def sls7(ctx):
    await ctx.send('SLS 7: https://youtu.be/GL16ck0nB7w')

@client.command()
async def sls8(ctx):
    await ctx.send('SLS 8: https://youtu.be/IIlHERIYS9s')

@client.command()
async def sls9(ctx):
    await ctx.send('SLS 9: https://youtu.be/bNq79vmZLb0')

@client.command()
async def sls10(ctx):
    await ctx.send('SLS 10: https://youtu.be/k-Pfsv9oYmA')

@client.command()
async def sls11(ctx):
    await ctx.send('SLS 11: https://youtu.be/2bWAwH5tXyM')

@client.command()
async def sls12(ctx):
    await ctx.send('SLS 12: https://youtu.be/e96HEzZGjrI')

@client.command()
async def sls13(ctx):
    await ctx.send('SLS 13: https://youtu.be/lGPHTC-jdU8')


# ATTACHES LINKS FOR POPULAR CVS/SOLOS/PROMOS
# @client.command()
# async def controversial_cv(ctx):
#     await ctx.send('idfk')


# IMPORTS COGS
for filename in os.listdir('./cogs'):
    if filename.endswith('s.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# RUNS BOT
client.run(os.getenv('DISCORD_TOKEN'))

import discord
from discord.ext import commands
import asyncio
import random
import os

class Tricks(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def how_to(self, ctx, trick):
        for x in tricks:
            if x == trick:
                if x == 'thumbaround':
                    await ctx.send('Thumbaround Tutorial: \nhttps://youtu.be/vEvPPVCH6cg')
                elif x == 'sonic':
                    await ctx.send('Sonic Tutorial: \nhttps://youtu.be/ueeZ3W7DIQo')
                elif x == 'charge':
                    await ctx.send('Charge Tutorial: \nhttps://youtu.be/AIe1jCYFNw0')
                elif x == 'twisted sonic':
                    await ctx.send('Twisted Sonic Tutorial: \nhttps://youtu.be/lCPB05Hifhw')
                elif x == 'backaround':
                    await ctx.send('Backaround Tutorial: \nhttps://youtu.be/DaOCyWGZRCM')
                elif x == 'scizzor spin':
                    await ctx.send('Scizzor Spin Tutorial: \nhttps://youtu.be/PUTTwcuzC1U')


tricks = ['thumbaround',
    'charge',
    'sonic',
    'fingerpass',
    'thumbaround reverse'
    'charge reverse',
    'sonic reverse',
    'fingerpass reverse',
    'neosonic',
    'neosonic reverse',
    'inverse sonic',
    'inverse sonic reverse',
    'wiper',
    'wiper reverse',
    'twisted sonic',
    'twisted sonic reverse',
    'backaround',
    'bust',
    'indexaround',
    'indexaround reverse',
    'fingless thumaround',
    'fingerless thumbaround reverse',
    'scizzor spin',
    'extended thumbaround',
    'extended thumbaround reverse',
    'neobackaround']


def setup(client):
    client.add_cog(Tricks(client))

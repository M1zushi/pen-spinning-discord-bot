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
                # Fundementals
                if x == 'thumbaround' or x == 'ta':
                    await ctx.send('Thumbaround Tutorial: \nhttps://youtu.be/vEvPPVCH6cg')
                elif x == 'sonic':
                    await ctx.send('Sonic Tutorial: \nhttps://youtu.be/ueeZ3W7DIQo')
                elif x == 'fingerpass' or x == 'fp':
                    await ctx.send('Fingerpass Tutorial: \nhttps://youtu.be/0EuJwfJHTyI')
                elif x == 'charge':
                    await ctx.send('Charge Tutorial: \nhttps://youtu.be/AIe1jCYFNw0')

                # Fundementals Reverse
                elif x == 'thumbaround reverse' or x == 'ta rev' or x == 'rev ta':
                    await ctx.send('Thumbaround Reverse Tutorial: \nhttps://youtu.be/gAf0BbipZ-I')
                elif x == 'sonic reverse':
                    await ctx.send('Sonic Reverse Tutorial: \nhttps://youtu.be/5nh_cXf71l8')
                elif x == 'fingerpass reverse' or x == 'fp rev' or x == 'rev fp':
                    await ctx.send('Fingerpass Reverse Tutorial: \nhttps://youtu.be/-BLoyJtbpn8')
                elif x == 'charge reverse':
                    await ctx.send('Charge Reverse Tutorial: \nhttps://youtu.be/kGyShNYrPhs')

                # Mega's Basics
                elif x == 'twisted sonic':
                    await ctx.send('Twisted Sonic Tutorial: \nhttps://youtu.be/lCPB05Hifhw')
                elif x == 'backaround':
                    await ctx.send('Backaround Tutorial: \nhttps://youtu.be/DaOCyWGZRCM')
                elif x == 'scizzor spin':
                    await ctx.send('Scizzor Spin Tutorial: \nhttps://youtu.be/PUTTwcuzC1U')
                elif x == 'neosonic':
                    await ctx.send('Neosonic: \nhttps://youtu.be/GnMmulpAMM8')

                # Mega's Basics Reverse
                # Trciks

                # Mega's Confirmed
                elif x == 'inverse sonic':
                    await ctx.send('Inverse Sonic: \nhttps://youtu.be/k0RhL8a4V9g')

                # Mega's Confirmed Reverse
                # Tricks

                # Mega's Advanced
                # Tricks

                # Mega's Advanced Reverse
                # Trick

                # Mega's Expert
                # Tricks

                # Mega's Expert Reverse
                # Tricks


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

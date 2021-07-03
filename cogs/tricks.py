import discord
from discord.ext import commands

import asyncio
import random

import os
import sys

class Tricks(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Fundementals
    @commands.command(aliases = ['ta'])
    async def thumbaround(self, ctx, mod='none'):
        if mod == 'none':
            await ctx.send('Thumbaround Tutorial: \nhttps://youtu.be/vEvPPVCH6cg')
        elif 'rev' in mod.lower():
            await ctx.send('Thumbaround Reverse Tutorial: \nhttps://youtu.be/gAf0BbipZ-I')

    @commands.command(aliases = ['fp'])
    async def fingerpass(self, ctx, mod='none'):
        if mod == 'none':
            await ctx.send('Fingerpass Tutorial: \nhttps://youtu.be/0EuJwfJHTyI')
        elif 'rev' in mod.lower():
            await ctx.send('Fingerpass Reverse Tutorial: \nhttps://youtu.be/-BLoyJtbpn8')

    @commands.command(aliases = [''])
    async def sonic(self, ctx, mod='none'):
        if mod == 'none':
            await ctx.send('Sonic Tutorial: \nhttps://youtu.be/ueeZ3W7DIQo')
        elif 'rev' in mod.lower():
            await ctx.send('Sonic Reverse Tutorial: \nhttps://youtu.be/5nh_cXf71l8')

    @commands.command(aliases = [''])
    async def charge(self, ctx, mod='none'):
        if mod == 'none':
            await ctx.send('Charge Tutorial: \nhttps://youtu.be/AIe1jCYFNw0')
        elif 'rev' in mod.lower():
            await ctx.send('Charge Reverse Tutorial: \nhttps://youtu.be/kGyShNYrPhs')


    # Mega's Basics
    @commands.command(aliases = ['tws', 'twisted sonic', 'twistedsonic'])
    async def twisted_sonic(self, ctx, mod='none'):
        if mod == 'none':
            await ctx.send('Twisted Sonic Tutorial: \nhttps://youtu.be/lCPB05Hifhw')

    @commands.command(aliases = ['bak'])
    async def backaround(self, ctx, mod='none'):
        if mod == 'none':
            await ctx.send('Backaround Tutorial: \nhttps://youtu.be/DaOCyWGZRCM')

    @commands.command(aliases = ['scizzor spin', 'scizzorspin'])
    async def scizzor_spin(self, ctx, mod='none'):
        if mod == 'none':
            await ctx.send('Scizzor Spin Tutorial: \nhttps://youtu.be/PUTTwcuzC1U')

    @commands.command(aliases = ['neo sonic'])
    async def neosonic(self, ctx, mod='none'):
        if mod == 'none':
            await ctx.send('Neosonic: \nhttps://youtu.be/GnMmulpAMM8')

    # Mega's Confirmed
    @commands.command(aliases = ['inverse sonic', 'inv sonic'])
    async def inverse_sonic(self, ctx, mod='none'):
        if mod == 'none':
            await ctx.send('Inverse Sonic: \nhttps://youtu.be/k0RhL8a4V9g')

    # Mega's Advanced


    # Mega's Expert



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

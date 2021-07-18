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
    @commands.command(name="Thumbaround", aliases=['ta'])
    async def _thumbaround(self, ctx, mod='none'):
        if mod == 'none':
            await ctx.send('__**Thumbaround Tutorial:**__ https://youtu.be/vEvPPVCH6cg')
        elif 'rev' in mod.lower():
            await ctx.send('__**Thumbaround Reverse Tutorial:**__ https://youtu.be/gAf0BbipZ-I')

    @commands.command(name="Fingerpass", aliases=['fp'])
    async def _fingerpass(self, ctx, mod='none'):
        if mod == 'none':
            await ctx.send('__**Fingerpass Tutorial:**__ https://youtu.be/0EuJwfJHTyI')
        elif 'rev' in mod.lower():
            await ctx.send('__**Fingerpass Reverse Tutorial:**__ https://youtu.be/-BLoyJtbpn8')

    @commands.command(name="Sonic", aliases=[])
    async def _sonic(self, ctx, mod='none'):
        if mod == 'none':
            await ctx.send('__**Sonic Tutorial:**__ https://youtu.be/ueeZ3W7DIQo')
        elif 'rev' in mod.lower():
            await ctx.send('__**Sonic Reverse Tutorial:**__ https://youtu.be/5nh_cXf71l8')

    @commands.command(name="Charge", aliases=[])
    async def _charge(self, ctx, mod='none'):
        if mod == 'none':
            await ctx.send('__**Charge Tutorial:**__ https://youtu.be/AIe1jCYFNw0')
        elif 'rev' in mod.lower():
            await ctx.send('__**Charge Reverse Tutorial:**__ https://youtu.be/kGyShNYrPhs')

    # Mega's Basics
    @commands.command(name="Twisted Sonic", aliases=['tws', 'twistedsonic', 'twisted'])
    async def _twisted_sonic(self, ctx, sonic='sonic', mod='none'):
        if 'sonic' in sonic.lower():
            if mod == 'none':
                await ctx.send('__**Twisted Sonic Tutorial:**__ https://youtu.be/lCPB05Hifhw')
            elif 'rev' in mod.lower():
                await ctx.send('')

    @commands.command(name="Backaround", aliases=['bak', 'cockaround'])
    async def _backaround(self, ctx, mod='none'):
        if mod == 'none':
            await ctx.send('__**Backaround Tutorial:**__ https://youtu.be/DaOCyWGZRCM')

    @commands.command(name="Scizzor Spin", aliases=['scizzor', 'scizzorspin'])
    async def _scizzor_spin(self, ctx, spin='spin', mod='none'):
        if 'spin' in spin.lower():
            if mod == 'none':
                await ctx.send('__**Scizzor Spin Tutorial:**__ https://youtu.be/PUTTwcuzC1U')

    @commands.command(name="Neosonic", aliases=['neo'])
    async def _neosonic(self, ctx, sonic='sonic', mod='none'):
        if 'sonic' in sonic.lower():
            if mod == 'none':
                await ctx.send('__**Neosonic:**__ https://youtu.be/GnMmulpAMM8')

    # Mega's Confirmed
    @commands.command(name="Inverse Tricks", aliases=['inv', 'inverse'])
    async def _inverse_tricks(self, ctx, trick, mod='none'):
        if 'sonic' in trick.lower():
            if mod == 'none':
                await ctx.send('__**Inverse Sonic:**__ https://youtu.be/k0RhL8a4V9g')
            elif 'rev' in mod.lower():
                await ctx.send('__**Inverse Sonic Reverse:**__ link')

    # Mega's Advanced


    # Mega's Expert



def setup(client):
    client.add_cog(Tricks(client))

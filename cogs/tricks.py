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
            await ctx.send('__**Thumbaround Tutorial:**__ https://youtu.be/vEvPPVCH6cg \n Starting Position Reference by Tombuto:')
            await ctx.send(file=discord.File('pics/ta_startingpos_by_Tombuto.jpg'))

        elif 'rev' in mod.lower():
            await ctx.send('__**Thumbaround Reverse Tutorial:**__ https://youtu.be/gAf0BbipZ-I')
            await ctx.send(file=discord.File('pics/ta_rev_startingpos_by_Tombuto.jpg'))

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

    # Basics
    @commands.command(name="Figure 8", aliases=['figure'])
    async def _figure8(self, ctx, name='8'):
        if '8' in name.lower():
            await ctx.send('__**Figure 8 Tutorial:**__ https://youtu.be/X3fuisvrrh0')

    @commands.command(name="Twisted Sonic", aliases=['tws', 'twistedsonic', 'twisted'])
    async def _twisted_sonic(self, ctx, sonic='sonic', mod='none'):
        if 'sonic' in sonic.lower():
            if mod == 'none':
                await ctx.send('__**Twisted Sonic Tutorial:**__ https://youtu.be/lCPB05Hifhw')

            elif 'rev' in mod.lower():
                await ctx.send('__**Twisted Sonic Reverse Tutorial:**__ https://youtu.be/d_OVOZh1Bc4')

            elif 'bust' in mod.lower():
                await ctx.send('__**Twisted Sonic Bust Tutorial:**__ https://youtu.be/lCPB05Hifhw')

        elif 'rev' in sonic.lower():
            await ctx.send('__**Twisted Sonic Reverse Tutorial:**__ https://youtu.be/d_OVOZh1Bc4')

        elif 'bust' in sonic.lower():
                await ctx.send('__**Twisted Sonic Bust Tutorial:**__ https://youtu.be/lCPB05Hifhw')


    @commands.command(name="Backaround", aliases=['bak', 'cockaround'])
    async def _backaround(self, ctx, mod='none'):
        if mod == 'none':
            await ctx.send('__**Backaround Tutorial:**__ https://youtu.be/DPFTVavvLfI \n``NOTE: Backaround = Korean Backaround = Bak``')

        elif mod == 'all':
            await ctx.send('__**Mid, Ring, Pinky Backarounds Tutorial:**__ https://youtu.be/XsNjUuM2Oo0')

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

            elif 'rev' in mod.lower():
                await ctx.send('__**Neosonic Reverse**__ https://youtu.be/QXFrR67JqFg')

    # Confirmed
    @commands.command(name="Inverse Sonic", aliases=['inv', 'inverse'])
    async def _inverse_sonic(self, ctx, trick, mod='none'):
        if 'sonic' in trick.lower():
            if mod == 'none':
                await ctx.send('__**Inverse Sonic:**__ https://youtu.be/k0RhL8a4V9g')

            elif 'rev' in mod.lower():
                await ctx.send('__**Inverse Sonic Reverse:**__ https://youtu.be/EO-_wZKh494')

    @commands.command(name="Shadow")
    async def _shadow(self, ctx, mod='none'):
        if mod == 'none':
            await ctx.send('__**Shadow:**__ https://youtu.be/T1OZvb5dKqE')

        elif 'rev' in mod.lower():
            await ctx.send('__**Shadow Reverse:**__ https://youtu.be/nC13FIuldHg')

    @commands.command(name="Bust")
    async def _bust(self, ctx):
        await ctx.send('''__**Bust:**__ https://youtu.be/T1OZvb5dKqE
        \n``NOTE: FOR TWISTED SONIC BUST USE TWS BUST
        (OR ANY OTHER TWS COMMAND ALIAS FOLLOWED BY BUST)``''')

    # Advanced
    @commands.command(name="Power Pass", aliases=['power', 'pp'])
    async def _powerpass(self, ctx, name='pass'):
        if 'pass' in name.lower():
            await ctx.send('__**Power Pass Tutorial:**__ https://youtu.be/-MtXqISQow0')

    # Expert
    @commands.command(name="Spider Spin", aliases=['spider', 'ss'])
    async def _spiderspin(self, ctx, name='spin'):
        if 'spin' in name.lower():
            await ctx.send('__**Spider Spin Tutorial:**__ https://youtu.be/7aZjnTooH1Q')

    @commands.command(name="Hai Tua", aliases=['hai'])
    async def _haitua(self, ctx, name='tua'):
        if 'tua' in name.lower():
            await ctx.send('__**Hai Tua Tutorial:**__ https://youtu.be/zd2Sx7bU5qQ')

    # More Power Tricks


    # More Common Hybrids
    @commands.command(name="Demon Sonic", aliases=['demonsonic', 'demon'])
    async def _demon_sonic(self, ctx, sonic='sonic'):
        if 'sonic' in sonic.lower():
            await ctx.send('__**Demon Sonic Tutorial:**__ https://youtu.be/W72RR6DdUyA')

    @commands.command(name="Angel Sonic", aliases=['angelsonic', 'angel'])
    async def _angel_sonic(self, ctx, sonic='sonic'):
        if 'sonic' in sonic.lower():
            await ctx.send('__**Angel Sonic Tutorial:**__ https://youtu.be/YWr_Pbhtd5g')

    # Counter Tricks


    # Fingercross?


    # Coolio
    @commands.command(name="Bakflip", aliases=[])
    async def _bakflip(self, ctx):
        await ctx.send('__**Bakflip Tutorial:**__ https://youtu.be/o6G6IxyMjPI')

    @commands.command(name="Seasick", aliases=[])
    async def _seasick(self, ctx):
        await ctx.send('__**Seasick Tutorial:**__ https://youtu.be/_6LIkOSygYk')

    @commands.command(name="Menowa 🤙 Stall", aliases=['🤙'])
    async def _menowarockstall(self, ctx):
        await ctx.send('__**🤙 Menowa Stall Tutorial 🤙 :**__ https://youtu.be/hanDBvlPjlE')


def setup(client):
    client.add_cog(Tricks(client))

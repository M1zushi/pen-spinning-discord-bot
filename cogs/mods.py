import discord
from discord.ext import commands

import asyncio
import requests
from pyquery import PyQuery

import re
import os
import sys


class Mods(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="Mod Search Command", aliases=['mod'])
    async def _modsearch(self, ctx, *, mod: str):
        pq = PyQuery(requests.get(
            'https://penmodding.pm/', params={'s': mod}).text)
        html = pq(
            '#general-wrapper div.col-lg-8.col-md-12.col-sm-12.col-xs-12.site-content-left.fixed-sidebar > div > div:first').html()

        res = {
            'url': re.search(r'image.*?a href=\"(.*?)\"', html).group(1),
            'img_url': re.search(r'img src=\"(.*?)\"', html).group(1),
            'title': re.search(r'title=\"(.*?)\"', html).group(1)
        }

        await ctx.send(f'{res["title"]} - {res["url"]}')


def setup(client):
    client.add_cog(Mods(client))

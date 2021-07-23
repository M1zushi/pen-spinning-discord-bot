import discord
from discord.ext import commands

import asyncio
import requests
from pyquery import PyQuery

# import pandas as pd

import re
import os
import sys


class Mods(commands.Cog):

    def __init__(self, client):
        self.client = client

    # # FUTURE ALGORITHM
    # @commands.command(name="MODSEARCHCOMMAND", aliases=['mod'])
    # async def _modsearch(self, ctx, arg):
    #
    #     # Func to search for <arg> on penmodding.pm
    #         top_result = {first_result}
    #
    #     try # Search func:
    #         await ctx.send(f'{arg}: {top_result})
    #     except # Results not found:
    #         await ctx.send('``! Please input a valid mod name !``')

    @commands.command(name="Mod Search Command", aliases=['mod'])
    async def _modsearch(self, ctx, mod: str):
        try:
            pq = PyQuery(requests.get(
                'https://penmodding.pm/', headers={'s': mod}).text)
            html = pq(
                '#general-wrapper div.col-lg-8.col-md-12.col-sm-12.col-xs-12.site-content-left.fixed-sidebar > div > div:first').html()

            res = {
                'url': re.search(r'image.*?a href=\"(.*?)\"', html).group(1),
                'img_url': re.search(r'img src=\"(.*?)\"', html).group(1),
                'title': re.search(r'title=\"(.*?)\"', html).group(1)
            }
            # modlink = modsearch(mod)

            await ctx.send(f'{res["title"]} - {res["url"]}')

        except Exception as e:
            await ctx.send(f"Something went wrong. Traceback:```\n{e}```")


def setup(client):
    client.add_cog(Mods(client))

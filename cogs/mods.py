import discord
from discord.ext import commands

import asyncio
import requests
import urllib

# import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession

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
    async def _modsearch(self, ctx, mod):

        def source(url):

            try:
                session = HTMLSession()
                response = session.get(url)
                return response

            except requests.exceptions.RequestException as e:
                print(e)

        def modsearch(query):

            query = urllib.parse.quote_plus(query)
            response = source("https://penmodding.pm/?s=" + query)
            results = list(response.html.absolute_links)
            penmodding_domain = ('https://penmodding.')

            for url in links[:]:
                if not url.startswith(penmodding_domain):
                    links.remove(url)
            #     elif query not in url:
            #         links.remove(url)

            return results[0]

        modlink = modsearch(mod)

        await ctx.send(f'{modlink}')


def setup(client):
    client.add_cog(Mods(client))

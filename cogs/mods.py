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

    # def get_source(url):
    # """Return the source code for the provided URL.
    #
    # Args:
    #     url (string): URL of the page to scrape.
    #
    # Returns:
    #     response (object): HTTP response object from requests_html.
    # """
    #
    # try:
    #     session = HTMLSession()
    #     response = session.get(url)
    #     return response
    #
    # except requests.exceptions.RequestException as e:
    #     print(e)
    #

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
            links = list(response.html.absolute_links)
            penmodding_domain = ('https://penmodding.')

            for url in links[:]:
                if not url.startswith(penmodding_domain):
                    links.remove(url)

        modlink = modsearch(mod)

        await ctx.send(f'{modlink}')


def setup(client):
    client.add_cog(Mods(client))

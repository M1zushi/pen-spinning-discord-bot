# BOT TESTING SERVER LINK:
# https://discord.gg/UEwf6RWqU2
# Created by: Mizu (M1zushi)

import os

# PACKAGES & IMPORTS
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv('.env')


class EmbedHelpCommand(commands.HelpCommand):
    # Set the embed colour here
    COLOUR = discord.Colour(0Xb8f2f2)

    def get_ending_note(self):
        return 'Use {0}{1} [command] for more info on a command.'.format(self.clean_prefix, self.invoked_with)

    def get_command_signature(self, command):
        return '{0.qualified_name} {0.signature}'.format(command)

    async def send_bot_help(self, mapping):
        embed = discord.Embed(title='Bot Commands', colour=self.COLOUR)
        description = self.context.bot.description
        if description:
            embed.description = description
        embed.set_author(name=client.user.name,
                         icon_url=client.user.avatar_url)

        for cog, commands in mapping.items():
            name = '\u200b' if cog is None else cog.qualified_name
            filtered = await self.filter_commands(commands, sort=True)
            if filtered:
                value = '\n'.join(
                    f"{f'** {c.name} **'.ljust(20, ' ')} -\t{c.brief}" for c in commands)
                if cog and cog.description:
                    value = '{0}\n{1}'.format(cog.description, value)

                embed.add_field(name=name, value=value)

        embed.set_footer(text=self.get_ending_note())
        await self.get_destination().send(embed=embed)

    async def send_cog_help(self, cog):
        embed = discord.Embed(
            title='{0.qualified_name} Commands'.format(cog), colour=self.COLOUR)
        embed.set_author(name=client.user.name,
                         icon_url=client.user.avatar_url)

        if cog.description:
            embed.description = cog.description

        filtered = await self.filter_commands(cog.get_commands(), sort=True)
        for command in filtered:
            embed.add_field(name=self.get_command_signature(
                command), value=command.short_doc or '...', inline=False)

        embed.set_footer(text=self.get_ending_note())
        await self.get_destination().send(embed=embed)

    async def send_group_help(self, group):
        embed = discord.Embed(title=group.qualified_name, colour=self.COLOUR)
        embed.set_author(name=client.user.name,
                         icon_url=client.user.avatar_url)
        if group.help:
            embed.description = group.help

        if isinstance(group, commands.Group):
            filtered = await self.filter_commands(group.commands, sort=True)
            for command in filtered:
                embed.add_field(name=self.get_command_signature(
                    command), value=command.short_doc or '...', inline=False)

        embed.set_footer(text=self.get_ending_note())
        await self.get_destination().send(embed=embed)

    # This makes it so it uses the function above
    # Less work for us to do since they're both similar.
    # If you want to make regular command help look different then override it
    send_command_help = send_group_help


# SETS UP BASICS
client = commands.Bot(command_prefix=('ps ', 'ps'),
                      case_insensitive=True,
                      activity=discord.Activity(
                          type=discord.ActivityType.playing, name='sls spam'),
                      status=discord.Status.dnd,
                      help_command=EmbedHelpCommand(),
                      )


# client.remove_command('help')


@client.event
async def on_ready():
    print('Time to spam sls.')


@client.command(name="ping", brief="Shows bot latency",
help="Type ``ping`` after the respective prefix to see the bot's latency.")
async def _ping(ctx):
    await ctx.send(f'Pen is spinning {round(client.latency * 1000)}ms late.')


@client.command(name="drop", brief="Dev only",
help="A command for me to shutdown the bot through discord, limited by ID")
async def _drop(ctx):
    if ctx.author.id in {int(os.getenv('MIZU_ID'))}:
        await ctx.send('I dropped my mod...')
        await client.logout()
    elif ctx.author.id in {int(os.getenv('MANDER'))}:
        why = {str(os.getenv('NO'))}
        await ctx.send(f'{why}')
    else:
        await ctx.send('I only listen to Mizu-kun!')


# ATTACHES POSTS ABOUT LEARNING ORDER
@client.command(name="Trick Order", aliases=["trickorder"],
brief='Attaches trick order made by Mega[FPSB]',
help='Attaches a trick order post made by french spinner Mega, in which he orders tricks by learning priority')
async def _trickorder(ctx):
    await ctx.send(file=discord.File('pics/megatrickorder.png'))


@client.command(name="Isuk Trick Order", aliases = ['isuktrickorder'],
brief='Attachs isuk\'s power trick difficulty categorization/trick order',
help='Attaches the link to isuk\'s blog inwhich he goes categorizes power tricks & links by difficulty, proving to be useful as a power trick order')
async def _isuktrickorder(ctx):
    await ctx.send('http://isukps.blogspot.com/2017/01/power-trick-learning-and-difficulty.html')


# INVITES TO DISCORD PS SERVERS
@client.command(name="Discord Workshop", aliases=['dworkshop'])
async def _discord_workshop(ctx):
    await ctx.send('https://discord.gg/aCtV5ZAu9X')


@client.command(name="Discord Reddit Server", aliases=['dreddit'])
async def _discord_reddit(ctx):
    await ctx.send('https://discord.gg/9bVNK8mefb')


@client.command(name="Discord Penstock", aliases=['dpenstock'])
async def _discord_penstock(ctx):
    await ctx.send('https://discord.gg/BxfewGYbQM')


@client.command(name="Discord International Penmodding Community", aliases=['dipmc'])
async def _discord_penmodding(ctx):
    await ctx.send('https://discord.gg/vXVWZz6UCv')


@client.command(name="Discord Mango Server", aliases=['dmango'])
async def _discord_mango(ctx):
    await ctx.send('https://discord.gg/Hrg6FHf')


@client.command(name="Discord Fenspinner", aliases=['dfen'])
async def _discord_fenspinner(ctx):
    await ctx.send('https://discord.gg/U3CpbYY3fP')


@client.command(name="Discord French Board", aliases=['dfpsb'])
async def _discord_french(ctx):
    await ctx.send('https://discord.gg/zSWBsd4c3b')


@client.command(name="Discord ThaiSpinner", aliases=['dthai'])
async def _discord_thai(ctx):
    await ctx.send('https://discord.gg/QjGZh2t')


@client.command(name="Discord Polish Board", aliases=['dpolish'])
async def _discord_polish(ctx):
    await ctx.send('https://discord.gg/MCXEnkh')


@client.command(name="Discord German Community", aliases=['dgpc'])
async def _discord_german(ctx):
    await ctx.send('https://discord.com/invite/aUuz8sh')


@client.command(name="Discord BirthdayCrimes", aliases=['dbc', 'dbirthdaycrimes'])
async def _discord_birthdaycrimes(ctx):
    await ctx.send('https://discord.gg/mYkh4nu9Uv')


# ATTACHES EXPLANATION FOR PS NOTATIONS
@client.command(name="Notation")
async def _notation(ctx):
    await ctx.send('''```In Pen Spinning, to write down "areas of the hand" in a trick or linkage,
    we use what is commonly reffered to as 'notaiton'.

```''')


# ATTACHES LINKS FOR PS LINKAGES
@client.command(name="Breakdown Generator", aliases=['bdg'])
async def _breakdowngenerator(ctx):
    await ctx.send('https://limezzje.github.io/PS/')


@client.command(name="SLS")
async def _sls(ctx):
    await ctx.send('Playlist: https://youtube.com/playlist?list=PLqvo4PPYx7nU8j3Cjz2u6dZ7s0FERNJ7y')


@client.command(name="SLS1")
async def _sls1(ctx):
    await ctx.send('SLS 1: https://youtu.be/a7AoLeswfuU')


@client.command(name="SLS2")
async def _sls2(ctx):
    await ctx.send('SLS 2: https://youtu.be/S0XiczC333A')


@client.command(name="SLS3")
async def _sls3(ctx):
    await ctx.send('SLS 3: https://youtu.be/7sSxBwdLsz0')


@client.command(name="SLS4")
async def _sls4(ctx):
    await ctx.send('SLS 4: https://youtu.be/JAnskN6yrI4')


@client.command(name="SLS5")
async def _sls5(ctx):
    await ctx.send('SLS 5: https://youtu.be/sTGL8CwVmUU')


@client.command(name="SLS6")
async def _sls6(ctx):
    await ctx.send('SLS 6: https://youtu.be/O0pGMTkd1X8')


@client.command(name="SLS7")
async def _sls7(ctx):
    await ctx.send('SLS 7: https://youtu.be/GL16ck0nB7w')


@client.command(name="SLS8")
async def _sls8(ctx):
    await ctx.send('SLS 8: https://youtu.be/IIlHERIYS9s')


@client.command(name="SLS9")
async def _sls9(ctx):
    await ctx.send('SLS 9: https://youtu.be/bNq79vmZLb0')


@client.command(name="SLS10")
async def _sls10(ctx):
    await ctx.send('SLS 10: https://youtu.be/k-Pfsv9oYmA')


@client.command(name="SLS11")
async def _sls11(ctx):
    await ctx.send('SLS 11: https://youtu.be/2bWAwH5tXyM')


@client.command(name="SLS12")
async def _sls12(ctx):
    await ctx.send('SLS 12: https://youtu.be/e96HEzZGjrI')


@client.command(name="SLS13")
async def _sls13(ctx):
    await ctx.send('SLS 13: https://youtu.be/lGPHTC-jdU8')


# ATTACHES LINKS FOR POPULAR CVS/SOLOS/PROMOS
# @client.command()
# async def controversial_cv(ctx):
#     await ctx.send('idfk')


# IMPORTS COGS
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# RUNS BOT
client.run(os.getenv('DISCORD_TOKEN'))

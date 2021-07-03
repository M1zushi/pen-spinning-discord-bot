from discord.ext import commands


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

    @commands.command(name="Twisted Sonic", aliases=['tws', 'twisted_sonic', 'twistedsonic'])
    async def _twisted_sonic(self, ctx, mod='none'):
        if mod == 'none':
            await ctx.send('__**Twisted Sonic Tutorial:**__ https://youtu.be/lCPB05Hifhw')

    @commands.command(name="Backaround", aliases=['bak'])
    async def _backaround(self, ctx, mod='none'):
        if mod == 'none':
            await ctx.send('__**Backaround Tutorial:**__ https://youtu.be/DaOCyWGZRCM')

    @commands.command(name="Scizzor Spin", aliases=['scizzor_spin', 'scizzorspin'])
    async def _scizzor_spin(self, ctx, mod='none'):
        if mod == 'none':
            await ctx.send('__**Scizzor Spin Tutorial:**__ https://youtu.be/PUTTwcuzC1U')

    @commands.command(name="Neosonic", aliases=['neo sonic'])
    async def _neosonic(self, ctx, mod='none'):
        if mod == 'none':
            await ctx.send('__**Neosonic:**__ https://youtu.be/GnMmulpAMM8')

    # Mega's Confirmed
    @commands.command(name="Inverse Sonic", aliases=['inverse_sonic', 'inv sonic'])
    async def _inverse_sonic(self, ctx, mod='none'):
        if mod == 'none':
            await ctx.send('__**Inverse Sonic:**__ https://youtu.be/k0RhL8a4V9g')

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

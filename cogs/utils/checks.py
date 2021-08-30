from discord.ext import commands


def is_mod():
    async def pred(ctx):
        return await check_guild_permissions(ctx, {'manage_guild': True})

    return commands.check(pred)


def admin_or_permissions(**perms):
    perms['administrator'] = True

    async def predicate(ctx):
        return await check_guild_permissions(ctx, perms, check=any)

    return commands.check(predicate)

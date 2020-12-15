from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def uso(ctx):
    await ctx.send('なんだろう嘘つくのやめてもらっていいですか')
    
@bot.command()
async def takuma(ctx):
    await ctx.send(':takumakaranopurezento:')

    


bot.run(token)

from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='km_')
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

@bot.command()
async def urnlo(ctx):
    await ctx.send('子供がいるとは思えないほどの華奢で処女の欲求不満な敏感爆乳魅力ママのうるんるちゃんの愛情たっぷり朝一絞りたての至極の母乳小便をお口の中にぴゅっぴゅされながら義務教育を終えたい')   

@bot.command()
async def kakikama(ctx):
    await ctx.send('手コキフェラパイずりしながらイっちゃえ:heart:イっちゃえ:heart:って言ってくるドSで押しに弱いチ●ポ大好きっ娘ご奉仕生意気■リ乳ムチムチ色白正統派黒髪清楚美少女かきかまちゃんとイチャラブ本気▲ませ交尾コンドーム突き破り中出し乳ブルンブルンベロチュー体液汁だくだくべちゃ濡れセックスしたい')

bot.run(token)

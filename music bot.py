import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=';;')


@bot.event
async def on_ready():
    print(">> Bot is online <<")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(710724588379832331)
    await channel.send(f'{member}歡迎家入♡')


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(710724588379832331)
    await channel.send(f'{member}留下來嘛!')

bot.run('NzEwNTE5NjEzNDYwMzE2MjQw.Xr4eXg.nHTsHEs1mKGPTFGlZDUtHiHilAw')

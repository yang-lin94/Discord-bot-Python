import discord
from discord.ext import commands
import json

with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix=';;')


@bot.event
async def on_ready():
    print(">> Bot is online <<")


@bot.command()
async def p(ctx):
    await ctx.send('音樂模式開發中')

bot.run(jdata['TOKEN'])

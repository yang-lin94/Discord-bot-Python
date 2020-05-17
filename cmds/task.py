import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import asyncio
import datetime


class task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


def setup(bot):
    bot.add_cog(Task(bot))

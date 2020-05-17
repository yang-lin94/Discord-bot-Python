import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import asyncio
import datetime


class task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def interval():
        await self.bot.wait_until_realy()
        while not self.bot.is_closed():


def setup(bot):
    bot.add_cog(Task(bot))

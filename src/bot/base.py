import discord

from discord.ext import commands

class Bot(commands.Bot):
    def __init__(self, token: str, intents: discord.Intents):
        self.token = token
        self.ready = False

        super().__init__(command_prefix='/', intents=intents)

    async def on_ready(self):
        self.ready = True

    async def connect_and_run(self):
        await self.start(self.token, reconnect = True)
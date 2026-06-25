import discord
from discord. ext import commands import os
from keep_alive import keep_alive
TOKEN = os. geten('BOT_TOKEN' )
intents = discord.Intents.default ()
intents.message_content = True
bot =
commands.Bot (command_prefix="!", intents=intents)
abot.event
async def on_ready ():
print(f'We have logged in as
{bot.user}')
keep_alive ()
bot. run(TOKEN)

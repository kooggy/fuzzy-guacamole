import discord
from discord.ext import commands
import luawl
import html2text
import requests
luawl.luawl_token = '215139f049945d9e3a4126e22781892eea176fb1'
intents = discord.Intents().all()
intents.members = True

client = commands.Bot(
    command_prefix='nigganutsack12345packerskooggynigganutskeaeaeeeeappoooooooocorrectkeyplssesndmethekey', intents=intents)
token = "MTA0NTUxMjg3ODcwNDMxMjMzMQ.GERwum.xgzMk91ALGXOP3nhstQcZERFyk9iVD47Nuah98"


@client.event
async def on_ready():
    print("Bot is online")


@client.event
async def on_message(message):
    if isinstance(message.channel, discord.channel.DMChannel):
        if message.content.startswith(".genKey"):
            await message.channel.send("Dm me the key you get from the link: https://workink.co/2iy/Key\n**DO NOT TRUST ANY POPUPS**")
        if message.content.startswith(requests.get("https://pastebin.com/raw/ZjzF8HYG").text):
            key = luawl.add_whitelist(str(message.author.id))
            await message.channel.send(f'**Correct Key**\nYour script is:\n```lua\n_G.wl_key = "{key}"\nrepeat wait() until game:isLoaded() task.wait(1)\nloadstring(game:HttpGet("https://scripts.luawl.com/13482/Ophelia.lua"))()```')
    else:
        if message.content.startswith(".genKey"):
            await message.channel.send("Dm me the key you get from the link: https://workink.co/2iy/Key\n**DO NOT TRUST ANY POPUPS**")
client.run(token)

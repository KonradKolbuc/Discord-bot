from dotenv import load_dotenv
from pathlib import Path
import os
import discord

load_dotenv(Path(__file__).parent / "config.env")
TOKEN = os.getenv("DISCORD_TOKEN")

'''
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
'''

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"I'm alive!")

    async def on_message(self, message):
        if message.author.bot:
            return
        if message.content == 'ping':
            await message.channel.send('pong')
        if message.content == 'oh':
            await message.channel.send('ah')
        if 'knock' in message.content:
            await message.channel.send("Who's there?")


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)

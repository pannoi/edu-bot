import discord
import os
import sys


client = discord.Client()
token = os.environ['DISCORD_TOKEN']

@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content.startswith('$hello'):
		await message.channel.send('Hello!')

client.run(token)
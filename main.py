import discord
import os
from src.docker import docker_help


client = discord.Client()
token = os.environ['DISCORD_TOKEN']


@client.event
async def on_ready():
	""" Printing that bot is ready. """
	print("Bot is ready to be used")


@client.event
async def on_message(message):
	""" Listening for messages in discrod channels and answers. """
	if message.content.find("ошибка с docker") != -1 or message.content.find("ошибка с докер") != -1:
		await message.channel.send('Specify the error with "docker help: "')
	if message.content.find("docker help: ") != -1:
		await message.channel.send(docker_help(message.content)) 


client.run(token)

import discord
import os
from src.docker import docker_help
from src.ansible import ansible_help
from src.git import git_help
from src.helm import helm_help
from src.jenkins import jenkins_help
from src.kubernetes import kubernetes_help
from src.molecule import molecule_help
from src.terraform import terraform_help


client = discord.Client()
token = os.environ['DISCORD_TOKEN']
if os.environ['CHANNEL_NAME']:
	channel = os.environ['CHANNEL_NAME']
else:
	channel = "general"


@client.event
async def on_ready():
	""" Printing that bot is ready. """
	print("Bot is ready to be used")


@client.event
async def on_message(message):
	""" Listening for messages in discrod channels and answers. """
	if message.content.find("ошибка с git") != -1 or message.content.find("ошибка с докер") != -1:
		await message.channel.send('Specify the error with "docker help: "')
	if message.content.find("git help: ") != -1:
		await message.channel.send(git_help(message.content))


client.run(token)

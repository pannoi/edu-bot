import discord
import os
import src.git as git_module

client = discord.Client()
token = os.environ['DISCORD_TOKEN']
channel = os.environ['CHANNEL_NAME']
git = git_module.git()


@client.event
async def on_ready():
	""" Printing that bot is ready. """
	print('Hey!')


@client.event
async def on_message(message):
	""" Listening for messages in discrod channels and answers. """
	if message.content.find("ошибка с") != -1 or message.content.find("Error") != -1:
		await message.channel.send('What error do you have -> provide "$ITEM help: "')
	if message.content.find("git help: ") != -1:
		await message.channel.send(git.git_help(message.content))


client.run(token)

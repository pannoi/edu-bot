import discord
import os
import src.git as git_module
import src.terraform as tf_module
import src.ansible as ansible_module
import src.docker as docker_module
import src.helm as helm_module
import src.jenkins as jenkins_module
import src.kubernetes as kubernetes_module
import src.molecule as molecule_module


client = discord.Client()
token = os.environ['DISCORD_TOKEN']
channel = os.environ['CHANNEL_NAME']
git = git_module.git()
tf = tf_module.tf()
ansible = ansible_module.ansible()
docker = docker_module.docker()
helm = helm_module.helm()
jenkins = jenkins_module.jenkins()
kubernetes = kubernetes_module.kubernetes()
molecule = molecule_module.molecule()


@client.event
async def on_ready():
	""" Printing that bot is ready. """
	print('Hey!')


@client.event
async def on_message(message):
	""" Listening for messages in discrod channels and answers. """
	if message.content.find("edu-bot help") != -1:
		await message.channel.send('What error do you have -> provide "$ITEM help: "')
	if message.content.find("git help: ") != -1:
		await message.channel.send(git.git_help(message.content))
	if message.content.find("terraform help: ") != -1:
		await message.channel.send(tf.tf_help(message.content))
	if message.content.find("ansible help: ") != -1:
		await message.channel.send(ansible.ansible_help(message.content))
	if message.content.find("docker help: ") != -1:
		await message.channel.send(docker.docker_help(message.content))
	if message.content.find("helm help: ") != -1:
		await message.channel.send(helm.helm_help(message.content))
	if message.content.find("jenkins help: ") != -1:
		await message.channel.send(jenkins.jenkins_help(message.content))
	if message.content.find("kubernetes helpl: ") != -1:
		await message.channel.send(kubernetes.kubernetes_help(message.content))
	if message.content.find("molecule help: ") != -1:
		await message.channel.send(molecule.molecule_help(message.content))


client.run(token)

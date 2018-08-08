import discord

TOKEN = ""

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

@client.event
async def on_message(message):
	if message.content.startswith("おはよう"):
		if client.user != message.author:
			m = "おはようございます" + message.author.name + "さん！"
			#print(message.author.name)
			if message.author.name == 'seruth':
				await client.send_message(message.channel, m)

@client.event
async def weather_report(message):
	pass

client.run(TOKEN)

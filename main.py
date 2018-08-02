import os
import random
import numpy as np
from discord.ext import commands

BOT_PREFIX = ("?", "!")

client = commands.Bot(command_prefix=BOT_PREFIX)

@client.command(description="与えられた任意の数の実数の和を返します", brief="数値の合計")

async def add(*num: float):
	await client.say(np.prod(num))

@client.command(description="n面体のサイコロをm回振ります。`!dice 12 5`のように指定してください。n, mの指定を省略すると6面のサイコロを1回振ります", brief="サイコロ")
async def dice(n: int = 6, m: int = 1) -> str:
	if n * m < 0:
		await client.say("nとmは両方とも1以上の整数で指定してください。")
	else:
		result = ', '.join(str(random.randint(1, n)) for r in range(m))
		await client.say(result)

@client.event
async def on_message(message):
	await client.process_commands(message)

	if client.user == message.author:
		return

	if message.content.startswith("こんにちは"):
		m = "こんにちは！" + message.author.name + "さん!\n"
		m = m + "`!add 1 1`のように入力すると、関数が実行できます！\n"
		m = m + "`?help`で実装されている関数の一覧を表示します!"
		await client.send_message(message.channel, m)

	if message.content.startswith("こんばんは"):
		m = "こんばんは！" + message.author.name + "さん！"
		await client.send_message(message.channel, m)

	if message.content.startswith("勉強した"):
		m = "えらい"
		await client.send_message(message.channel, m)

	@client.event
	async def on_ready():
		print('以下のユーザー名でログインしています')
		print('ユーザー名: ' + client.user.name)
		print('ユーザーid: ' + client.user.id)
		print('-------------------------------')

	client.run(os.environ.get("DISCORD_TOKEN"))

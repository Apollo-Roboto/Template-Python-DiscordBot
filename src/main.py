import asyncio
from discord.ext import commands
from discord import Intents

from dotenv import load_dotenv
import os

from controllers.StatusController import StatusController
from controllers.SyncController import SyncController

async def main():
	load_dotenv()

	bot = commands.Bot(
		command_prefix='!',
		intents=Intents.all(),
	)

	await bot.add_cog(SyncController(bot)) 
	await bot.add_cog(StatusController(bot)) 

	print("App Commands:")
	for command in bot.tree.walk_commands():
		print(f'\t{command.name}')
	print("Commands:")
	for command in bot.walk_commands():
		print(f'\t{command.name}')

	# bot.run(os.environ['DISCORD_BOT_TOKEN'])
	await bot.start(os.environ['DISCORD_BOT_TOKEN'])

if(__name__ == '__main__'):
	asyncio.run(main())
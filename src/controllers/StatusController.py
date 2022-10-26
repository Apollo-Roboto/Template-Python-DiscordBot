from discord.ext import commands
from discord import app_commands, Interaction # contains the slash commands

import psutil

from models.Status import Status
from views import StatusView

class StatusController(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(
		name='ping',
	)
	async def pingCommand(self, ctx):
		print('Ping received')
		await ctx.send('Pong')

	@app_commands.command(
		name='status',
		description='Display bot status',
	)
	async def statusCommand(self, interaction: Interaction) -> None:

		status = Status(
			ready=True,
			ram=psutil.virtual_memory().percent,
			cpu=psutil.cpu_percent(1),
		)

		embed = StatusView.view(status)

		# await ctx.send(embed=embed)

		await interaction.response.send_message(embed=embed)
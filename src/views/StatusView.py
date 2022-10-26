from discord import Embed, Color
from models.Status import Status

color = Color.from_str('#5865f2')

def view(status: Status):
	embed = Embed(color=color)
	embed.title = 'Current Status'
	embed.add_field(name='Ready', value=status.ready, inline=True)
	embed.add_field(name='CPU', value=f'{status.cpu}%', inline=True)
	embed.add_field(name='RAM', value=f'{status.ram}%', inline=True)
	return embed
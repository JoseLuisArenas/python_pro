import discord
import os
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?',
                   description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def meme(ctx):
    img_folder = 'M2L1/imagen'
    img_name = random.choice(os.listdir(img_folder))
    img_path = os.path.join(img_folder, img_name)
    with open(img_path, 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)


bot.run("MTE1OTY0MzY0NjExMTUzMTAxOQ.GhpuzE.CrqJHcDVI9ckykI7_TA0K6YMeTGNg3q8PqOWZo")
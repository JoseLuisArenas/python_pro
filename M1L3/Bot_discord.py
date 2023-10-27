import discord
import random
import math
from bot_logic import *



# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "Cara"
    else:
        return "Sello"
    
@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith("$pass"):
        await message.channel.send(gen_pass(10))

    elif message.content.startswith("$flip_coin"):
        flip_coin()
        


    else:
        await message.channel.send(message.content)


    
    



client.run("f49adeaed3b7745cf76bea0ec4a9af4d214aa2ccdc989b1874e8c03bd172a893")
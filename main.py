import discord 
import os

client = discord.Client()

@client.event
async def on_ready():
  print('Hola, mi nombre es {0.user}'.format(client))

@client.event
async def on_message(message,discordNewUser):
  if message.author == client.user:
    return
  
  msg = message.content
  if msg.startswith('$bv'):
    
    administrador = str(message.author)
    await message.channel.send('hola soy el administrador ' + administrador +' y te doy la bienvenida a este grupo ' + discordNewUser )

client.run(os.getenv('TOKEN'))

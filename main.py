import discord 
import os

client = discord.Client()

@client.event
async def on_ready():
  print('Hola, mi nombre es {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  msg = message.content
  if msg.startswith('$bv'):
    
    await message.channel.send("""hola y bienvenid@ a PuntoBlend. Esta es tu casa, pasa a leer la sección de #reglas y conocerás los términos de convivencia del grupo.
Puedes acceder a las diferentes secciones para disfrutar y compartir con la  comunidad. 
Si tienes alguna pregunta solemos hacerlo en #ayuda-en-blender, para tomar un café y charlar.. quedamos en ... #la-taberna-de-suzanne-offtopic.

Si no conoces el Discord y quieres saber cómo moverte en nuestra comunidad puedes ver el  siguiente video: https://www.youtube.com/watch?v=YBR_za_mJAU""" )

client.run(os.getenv('TOKEN'))

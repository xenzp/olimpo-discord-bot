import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/', description = 'im chuerking.')

@bot.command()
async def hola(ctx):
    await ctx.send('SAL DE MI PANTANO')

#Evento
@bot.event
async def on_ready():
    print('CHUERK IS READY ')
    await bot.change_presence(activity=discord.Streaming(name='CHUERKEANDO', url='www.twitch.tv/bgamerz4'))
        #EMBED MOTIVO BAN
@bot.command()
async def embed_ban(ctx):
    embed = discord.Embed(
        title= ':no_entry_sign: Motivos de baneo :no_entry_sign:',
        description = """ `1.0`| Mandar informacion personal de terceros (Fotos,datos,numeros de telefonos,etc) sin consentimiento
    `1.1`| Spam (Invitaciones,links,canales) al privado de los usuarios
    `1.2`| Mandar gore y contenido nsfw
    `1.3`| Reiteradas sanciones de menos gravedad de forma constante
    `1.4`| Acoso a miembros del servidor en mensajes privados
    `1.5`| El bardo y las jodas estan PERMITIDAS pero: No vamos a permitir el constante acoso sobre una sola persona en particular, sera motivo de ban permanente
    """,
        colour = discord.Colour.orange())
    await ctx.send(embed=embed)
        #EMBED MOTIVO MUTE
@bot.command()
async def embed_mute(ctx):
    embed = discord.Embed(
        title= ':mute: Motivos de muteo :mute:',
        description = """ `1.0`| Hacer flood en general (Multiples mensajes en cadena con motivo de molestar)
    `2.1`| Constante envio de imagenes en general del servidor
    `2.2`| Constante uso de bots
    `2.3`| Insultar, saturar o molestar en salas de voz
    `2.4`| Multiples tagueos al staff sin ninguna razon
    """,
        colour = discord.Colour.orange())
    await ctx.send(embed=embed)
    #VERIFICACION
@bot.command()
async def p_msg(ctx):
    autor = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.orange(),
        title = "HOLA AMIGO TE SALUDO",
    )
    await autor.send(embed=embed)




bot.run('NzUxMjUwODYzMjYzMTg3MDA1.X1GW4w.iz92CCgsGbxps2wvV7dzR3uCMCI')
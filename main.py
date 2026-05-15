import discord
from discord.ext import commands
from model import get_class
import os, random
import requests
import config
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
def get_duck_image_url():
    url = "https://random-d.uk/api/v2/random"
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command()
async def duck(ctx):
    """The duck command returns the photo of the duck"""
    print("hello")
    image_url = get_duck_image_url()
    await ctx.send(image_url)
@bot.command()
async def check(ctx):
    if not ctx.message.attachments:
        await ctx.send("Olvidaste subir una imagen.")
        return

    try:
        attachment = ctx.message.attachments[0]

        # Verificar formato
        if not attachment.filename.lower().endswith((".png", ".jpg", ".jpeg")):
            await ctx.send("Formato no válido. Usa PNG o JPG.")
            return

        # Guardar imagen
        image_path = f"./{attachment.filename}"
        await attachment.save(image_path)

        # Inferencia
        clase, confianza = get_class(
            model_path="./keras_model.h5",
            labels_path="./labels.txt",
            image_path=image_path
        )

        confianza = float(confianza)

        # Baja confianza
        if confianza < 0.70:
            await ctx.send(
                "Lo siento, no estoy seguro de lo que aparece en la imagen."
            )
            return

        # Respuesta
        await ctx.send(
            f"Objeto detectado: {clase}\n"
            f"Confianza: {confianza:.2%}"
        )

    except Exception as e:
        await ctx.send(
            f"Ocurrió un error durante la inferencia: {e}"
        )
bot.run(config.TOKEN)
import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
@bot.event
async def on_ready():
    print(f"🌎 EcoCreativo conectado: {bot.user}")


@bot.command()
async def hola(ctx):
    await ctx.send(
        "🌱 ¡Hola! Soy EcoCreativo.\n"
        "¡Vamos a convertir residuos en creaciones increíbles! ♻️"
    )


@bot.command()
async def ayuda(ctx):
    await ctx.send(
        "🤖 **COMANDOS DE ECOCREATIVO**\n\n"
        "🌱 *hola - Saludar al robot.\n"
        "📋 *ayuda - Ver los comandos.\n"
        "🧴 *botellas - Crear juguetes con botellas.\n"
        "📦 *carton - Crear objetos con cartón.\n"
        "🥫 *latas - Crear portalápices.\n"
        "🔵 *tapas - Crear juegos con tapas.\n"
        "🎨 *ideas - Obtener una idea sorpresa."
    )


@bot.command()
async def botellas(ctx):
    await ctx.send(
        "🚗 **PROYECTO: CARRO DE JUGUETE**\n\n"
        "Materiales:\n"
        "• 1 botella de plástico limpia.\n"
        "• 4 tapas para las ruedas.\n"
        "• 2 palitos para los ejes.\n"
        "• Cartón para decorar.\n\n"
        "Pasos:\n"
        "1. Limpia y seca la botella.\n"
        "2. Pide ayuda a un adulto para hacer los agujeros.\n"
        "3. Coloca los palitos como ejes.\n"
        "4. Fija las tapas como ruedas.\n"
        "5. Decora tu carro.\n\n"
        "¡Felicidades! Has creado un juguete reutilizando materiales. 🌎"
    )


@bot.command()
async def carton(ctx):
    await ctx.send(
        "🏠 **PROYECTO: CASA DE CARTÓN**\n\n"
        "Materiales:\n"
        "• Una caja de cartón.\n"
        "• Papel reutilizado.\n"
        "• Colores y pegamento.\n\n"
        "Pasos:\n"
        "1. Busca una caja limpia.\n"
        "2. Dibuja puertas y ventanas.\n"
        "3. Decora las paredes.\n"
        "4. Crea muebles pequeños con cartón.\n\n"
        "¡Ya tienes una casa para tus muñecos! 🎨"
    )


@bot.command()
async def latas(ctx):
    await ctx.send(
        "✏️ **PROYECTO: PORTALÁPICES**\n\n"
        "Materiales:\n"
        "• Una lata limpia y sin bordes cortantes.\n"
        "• Papel de colores.\n"
        "• Pegamento.\n\n"
        "Pasos:\n"
        "1. Pide a un adulto que prepare la lata.\n"
        "2. Decora el exterior con papel.\n"
        "3. Déjala secar.\n"
        "4. Coloca tus lápices.\n\n"
        "¡Ahora tienes un organizador ecológico! ♻️"
    )


@bot.command()
async def tapas(ctx):
    await ctx.send(
        "🎲 **PROYECTO: JUEGO DE MESA**\n\n"
        "Materiales:\n"
        "• Tapas de diferentes colores.\n"
        "• Un cartón reutilizado.\n"
        "• Marcadores.\n\n"
        "Pasos:\n"
        "1. Dibuja un tablero en el cartón.\n"
        "2. Utiliza las tapas como fichas.\n"
        "3. Inventa reglas para tu juego.\n\n"
        "¡Diviértete reutilizando! 🌱"
    )


@bot.command()
async def ideas(ctx):
    proyectos = [
        "🚗 Botellas = carros de juguete.",
        "🏠 Cajas = casas para muñecos.",
        "✏️ Latas = portalápices.",
        "🎲 Tapas = fichas para juegos.",
        "🧻 Rollos de cartón = binoculares de juguete."
    ]

    idea = random.choice(proyectos)

    await ctx.send(
        "🎨 **¡IDEA ECOLÓGICA SORPRESA!**\n\n"
        + idea
        + "\n\n♻️ ¡Dale una segunda vida a tus residuos!"
    )


bot.run("YOUR_BOT_TOKEN")


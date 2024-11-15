import discord
from discord.ext import commands
#from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
#load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Configurações do bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=",", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot está online como {bot.user}")

    channel_id = 1295104782209515601

    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send("Bot Online")

@bot.command()
async def ola(ctx):
    await ctx.reply(f"Olá, {ctx.author.mention}!03")

# Inicia o bot
bot.run("MTMwNjczMTk5Mzk5OTg3MjEzMQ.GJnHHO.X7oEfEXM86LTwYR_fSQ1tNp3FrtAUbcrEEuR-4")
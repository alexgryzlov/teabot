import discord
import asyncio
from discord.ext import commands
from os import environ

from download import download

TOKEN = environ["TEABOT_TOKEN"]



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="%", intents=intents)

@bot.command(aliases=["p", "з", "играй"])
async def play(ctx, *, name):
    audio_path = download(name)

    channel = ctx.author.voice.channel
    voice_client = await channel.connect()
    voice_client.play(
        discord.FFmpegPCMAudio(audio_path),
        after=lambda e: asyncio.run_coroutine_threadsafe(voice_client.disconnect(), bot.loop),
    )


@bot.command(aliases=["хватит"])
async def stop(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()

bot.run(token=TOKEN)

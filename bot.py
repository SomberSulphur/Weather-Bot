import logging
import discord
from discord.ext import commands

import os
import asyncio


intents=discord.Intents.all()
intents.message_content=True

bot=commands.Bot(command_prefix="-",intents=intents,help_command=None,case_insensitive=True)

cogs_to_load= ["cogs.weather"]

#i know its a shitty cog loader, idc tho :(
async def load():
    for cog in cogs_to_load:
        try:
            await bot.load_extension(cog)
            print(f"Loaded [{cog}]")
        except:
            logging.exception(f"Error during the loading of {cog}")

async def main():
    await load()
    await bot.start("your token here ig")

@bot.listen()
async def on_ready():
    print(f"Bot is online :) as {bot.user.name} | {bot.user.id}")

@bot.command()
async def sync(ctx):
    try:
        bot.tree.copy_global_to(guild=ctx.guild)
        await bot.tree.sync(guild=ctx.guild)
        print("synced")
    except:
        logging.exception("Error During tree syncing")

discord.utils.setup_logging()
asyncio.run(main())

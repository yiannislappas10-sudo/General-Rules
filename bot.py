import os

import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

from rules_view import RulesView

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = os.getenv("GUILD_ID")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.tree.command(name="rules", description="Show the community, game, and economy rules.")
async def rules(interaction: discord.Interaction):
    await interaction.response.send_message(view=RulesView())


@bot.event
async def setup_hook():
    if GUILD_ID:
        guild = discord.Object(id=int(GUILD_ID))
        bot.tree.copy_global_to(guild=guild)
        await bot.tree.sync(guild=guild)
    else:
        await bot.tree.sync()


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} - bot is online.")


if __name__ == "__main__":
    if not TOKEN:
        raise RuntimeError("DISCORD_TOKEN is not configured.")
    bot.run(TOKEN)

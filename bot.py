import logging
import os

import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

from rules_view import RulesView

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = os.getenv("GUILD_ID")
ALERT_USER_ID = int(os.getenv("ALERT_USER_ID", "1441030741998702592"))

logger = logging.getLogger(__name__)
_runtime_error_count = 0
_alert_sent = False

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


async def report_runtime_error(error: Exception, context: str) -> None:
    """Log errors and alert the configured owner once after six runtime errors."""
    global _runtime_error_count, _alert_sent
    _runtime_error_count += 1
    logger.exception("Runtime error in %s (error %d)", context, _runtime_error_count, exc_info=error)

    if _runtime_error_count <= 5 or _alert_sent:
        return

    try:
        user = bot.get_user(ALERT_USER_ID) or await bot.fetch_user(ALERT_USER_ID)
        await user.send(
            f"<@{ALERT_USER_ID}> the General-Rules bot has encountered "
            f"{_runtime_error_count} runtime errors. Latest context: {context}."
        )
        _alert_sent = True
        logger.warning("Sent runtime-error alert to user %s", ALERT_USER_ID)
    except (discord.DiscordException, ValueError) as alert_error:
        logger.error("Could not send runtime-error alert: %r", alert_error)


@bot.tree.error
async def on_app_command_error(
    interaction: discord.Interaction, error: app_commands.AppCommandError
):
    await report_runtime_error(error, "slash command")
    message = "Something went wrong while running that command."
    if interaction.response.is_done():
        await interaction.followup.send(message, ephemeral=True)
    else:
        await interaction.response.send_message(message, ephemeral=True)


@bot.event
async def on_error(event_method: str, *args, **kwargs):
    error = discord.ClientException(f"Unhandled error in event: {event_method}")
    await report_runtime_error(error, event_method)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} - bot is online.")


if __name__ == "__main__":
    if not TOKEN:
        raise RuntimeError("DISCORD_TOKEN is not configured.")
    bot.run(TOKEN)

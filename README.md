# General Rules bot

A Discord bot that publishes the community, in-game, and economy rules through a `/rules` slash command.

## Railway setup

1. Deploy this repository as a Railway service.
2. In **Variables**, add `DISCORD_TOKEN` and paste the bot token there. Do not put the real token in GitHub.
3. Add `GUILD_ID` with your Discord server ID for immediate command synchronization. Without it, global slash commands can take up to an hour to appear.
4. Invite the bot with both the `bot` and `applications.commands` scopes.
5. Give it permission to view/send messages and use application commands in the target channel.

The service starts with `python bot.py`.

## Runtime error alerts

Set `ALERT_USER_ID` to the Discord user ID that should receive one DM after the bot records more than five runtime errors in one process run. It defaults to `1441030741998702592`.

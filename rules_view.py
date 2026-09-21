import discord
from discord import ui

# ─────────────────────────────────────────────────────────────
# RULE TEXT — edit these freely
# ─────────────────────────────────────────────────────────────

DISCORD_RULES = """꧁ 𓆩✰༺☾ COMMUNITY STANDARDS ☽༻✰𓆪꧂

**I. Explicit & Graphic Content**
Points won't be removed even if you're unbanned. To comply with Discord's Community Guidelines, explicit or graphic content is strictly prohibited.
• Pornographic or sexually explicit media → Permanent Ban
• Sexual roleplay, erotic discussions, or explicit requests → Warning / Mute
• Suggestive images, cropped NSFW, or filter bypasses → Indefinite Ban
• Graphic gore, mutilation, or real-life violent content → Permanent & Non-Appealable Ban
• Content depicting abuse, torture, or cruelty → Permanent & Non-Appealable Ban

**II. Respect & Conduct**
Treat every member with respect regardless of disagreements.
• Harassing, bullying, or targeting members → Temporary to Indefinite Ban
• Discrimination, hate speech, or offensive remarks → Permanent & Non-Appealable Ban
• Threatening violence, self-harm, or credible threats → Permanent Ban
• Sexual harassment, predatory behavior, or unwanted advances → Permanent & Non-Appealable Ban
• Sharing private information (Doxxing) → Permanent & Non-Appealable Ban

**III. Spam & Disruptive Behavior**
Keep conversations readable and avoid intentionally disrupting the community.
• Spam, excessive emojis, repeated messages, or keyboard smashing → Warning
• Mass mentions (@everyone / @here) without permission → Warning / Temporary Mute
• Advertising servers, communities, or products → Temporary Ban
• Using alternate accounts to avoid punishments (Alt Evasion) → Permanent Ban (All Accounts)
• Intentionally disrupting chats, events, or roleplay → Warning / Mute / Ban

**IV. Exploits & Security**
Any attempt to abuse Discord or the community will be taken seriously.
• Malware, phishing links, token grabbers, or malicious software → Permanent & Non-Appealable Ban
• Scamming, impersonating, or deceiving for gain → Permanent Ban
• Exploiting bots, loopholes, or server vulnerabilities → Admin Discretion

**V. Appropriate Content**
Please keep discussions suitable for the community.
• Political or religious debates intended to provoke arguments → Warning
• Deliberately offensive or inflammatory content → Warning / Temporary Ban
• Impersonating staff members or trusted individuals → Indefinite Ban
• Posting misleading information while pretending it is official → Warning / Ban

**VI. Staff Decisions**
Our staff team is responsible for maintaining a fair and enjoyable community.
• Staff decisions should be respected at all times.
• If you disagree with a punishment, use the proper appeal process instead of arguing publicly.
• Attempting to evade punishments will result in harsher penalties.
• Staff reserve the right to act on harmful behavior not explicitly listed.

**VII. Links & Advertising**
Unsolicited or unwanted links are not allowed anywhere in the server.
• Sending unwanted/unsolicited links (invite links, spam links, redirect links, etc.) → Warning / Mute
• Repeated link spam after a warning → Temporary to Permanent Ban
• Malicious or disguised links (see Exploits & Security) → Permanent & Non-Appealable Ban

**VIII. Character & Content Ownership**
Respect what other members have created.
• Drawing, writing, animating, or otherwise using someone else's OC/character requires their permission first → Warning
• Claiming or "reskinning" another member's character concept without permission → Warning / Ban
• Always credit the original creator when referencing someone else's lore or OC → Warning

**IX. Anti-Drama**
Keep conflicts out of public spaces.
• Personal conflicts, callouts, or disputes must be taken to DMs or a support ticket, not aired in public channels → Warning
• Stirring drama or baiting others into public arguments → Warning / Temporary Mute"""

INGAME_RULES = """**§ ROBLOX GAME RULES §**
*Please read carefully before playing*
━━━━━━━━━━━━━━━━━━

**I. Roblox Compliance**
All Roblox Terms of Service and Community Standards apply at all times.
• Violating Roblox ToS/Community Standards → Warning / Ban (severity-based)

**II. No Exploiting**
Abusing bugs, glitches, or exploits for personal gain results in severe penalties, including permanent bans.
• Minor exploit for personal convenience → Temporary Ban
• Exploiting for unfair advantage or to harm others' experience → Permanent Ban

**III. Content Standards**
No suggestive, inappropriate, or controversial content — this includes usernames, outfits, builds, and chat.
• First offense → Warning + forced change
• Repeated offense → Temporary to Permanent Ban

**IV. No Trolling**
Deliberately disrupting roleplay, baiting reactions, or ruining others' experience for "fun" is forbidden.
• Warning / Temporary Mute, escalating to Ban for repeat offenders

**V. Respect & Conduct**
No harassment, stalking, discrimination, hate speech, or personal attacks. Treat others the way you'd want to be treated.
• Harassment/personal attacks → Warning / Temporary Ban
• Discrimination or hate speech → Permanent & Non-Appealable Ban

**VI. Fair Roleplay**
The following are considered Fail RP and are **not allowed**:
› **Meta Grudging** — Letting OOC conflict affect IC treatment of a player
› **Meta Gaming** — Using OOC knowledge your character has no way of knowing IC
› **God Modding** — Giving your character unfair/unbeatable traits, or controlling another player's character without consent
› **Combat Logging** — Leaving mid-conflict to dodge consequences
› **Power Gaming** — Forcing actions onto another player without giving them a chance to respond
• Any Fail RP violation → Warning, escalating to Temporary Ban for repeat offenders

**VII. No Advertising**
Do not advertise other games, Discord servers, or social media without staff permission.
• First offense → Warning + message removed
• Repeated advertising → Temporary Ban

**VIII. Staff Authority**
Staff decisions are final during active situations. Disputes go through proper channels (ticket/DM), not public arguments.
• Arguing publicly with staff → Warning / Temporary Mute

**IX. Age-Appropriate Themes**
Dark or mature myth themes (death, sacrifice, war, etc.) are allowed but must stay symbolic/non-graphic — no gore, excessive violence, or disturbing detail.
• Warning + content removal, escalating to Temporary Ban for repeat offenders

**X. One Character Rule**
Players may only control one primary character at a time unless given permission for NPCs.
• Warning + character correction

**XI. Consent for Major Actions**
Killing, kidnapping, or permanently altering another player's character requires their OOC consent first. This also covers drawing someone's OC or using them in animations/RP — ask first.
• Acting without consent → Warning, escalating to Temporary Ban for repeat offenders

**XII. Perma-Death Consent**
A character can only be permanently killed off with the player's explicit OOC agreement beforehand. No surprise perma-kills.
• Forcing a perma-kill without consent → Warning / Temporary Ban + action reversed

**XIII. Lore Consistency**
Players may not retcon or contradict established server lore to fit their own character or story — check with staff before introducing major lore changes.
• Warning + retcon reversed, escalating to Temporary Ban for repeat offenders"""

ECONOMY_RULES = """**Economy (Envy) Rules**

**I. No Real-Money Trading**
Envy or in-game items may not be bought, sold, or traded for real money or real-world goods.
• Exception: rewards given directly by an admin (e.g. Nitro, giveaway prizes) are allowed.
• Any player found RMT-ing → Permanent Ban + trade reversal

**II. No Exploiting**
Using bugs, glitches, or loopholes to duplicate currency or items, or to gain an unfair economic advantage → Permanent Ban + full point/currency wipe

**III. No Fake Listings**
Creating fake, misleading, or bait listings in the marketplace (including listings for items you don't actually have) → Warning / Temporary Ban + listing removed

**IV. Listings Must Go Through the Official System**
All trades and sales must be done through the proper listing/market command — no exceptions, no off-book side deals. Off-book trades are not covered by refund/support if something goes wrong.

**V. No Price Manipulation**
Colluding with alt accounts or other players to manipulate prices, or scalping listings to exploit new/inactive players → Warning / Temporary Ban

**VI. No Currency Farming via Alts**
Using alternate accounts to farm Envy, exploit daily/work rewards, or manipulate the market → Permanent Ban (All Accounts)

**VII. Scam Trades**
Deliberately scamming another player in a trade (not delivering after payment, swapping listed items, etc.) → Permanent Ban + trade reversed where possible

**VIII. Admin Discretion on Disputes**
Staff reserve the right to reverse, freeze, or cancel any trade/listing suspected of fraud, exploitation, or rule-breaking, even without a formal report."""

RULES = {
    "ingame": INGAME_RULES,
    "discord": DISCORD_RULES,
    "economy": ECONOMY_RULES,
}

POINT_INFO = (
    "• You may re-join only by *High Rank* approval.\n"
    "• You can apply with an apology.\n"
    "• Warnings/points are removed after 1 month.\n"
    "• If you get banned again, it will be **permanent with no excuse**."
)

PUNISHMENT_TABLE = (
    "**Minor rule break** — 1 pt → Verbal warning\n"
    "**Repeated minor breaks** — 2 pts → Written warning\n"
    "**Moderate offense** — 3 pts → 24h suspension\n"
    "**Serious offense** — 5 pts → 7-day suspension / demotion\n"
    "**6+ points total** → Removal from Security\n"
    "**Ban evasion / repeat ban** → **Permanent ban, no excuse**"
)


# ─────────────────────────────────────────────────────────────
# UI COMPONENTS
# ─────────────────────────────────────────────────────────────

def build_reply(title: str, body: str, color: discord.Colour = discord.Colour.dark_theme()) -> ui.LayoutView:
    """Wraps any block of rule text in a styled Components V2 container
    so ephemeral replies look like the main panel instead of a plain text dump."""
    view = ui.LayoutView()
    container = ui.Container(accent_color=color)
    container.add_item(ui.TextDisplay(f"# {title}"))
    container.add_item(ui.Separator())
    container.add_item(ui.TextDisplay(body))
    view.add_item(container)
    return view


class RuleSelect(ui.Select):
    def __init__(self):
        super().__init__(
            placeholder="Select the rule",
            options=[
                discord.SelectOption(label="In-Game Rules", value="ingame", emoji="🎮"),
                discord.SelectOption(label="Discord Rules", value="discord", emoji="💬"),
                discord.SelectOption(label="Economy Rules", value="economy", emoji="💰"),
            ],
        )

    async def callback(self, interaction: discord.Interaction):
        key = self.values[0]
        titles = {"ingame": "In-Game Rules", "discord": "Community Standards", "economy": "Economy (Envy) Rules"}
        view = build_reply(titles[key], RULES[key])
        # Only the person who clicked sees this — ephemeral=True
        await interaction.response.send_message(view=view, ephemeral=True)


class RulesView(ui.LayoutView):
    def __init__(self):
        super().__init__()
        container = ui.Container(accent_color=discord.Colour.dark_theme())

        container.add_item(ui.TextDisplay("# Project Heaven — Rules"))
        container.add_item(ui.TextDisplay(
            "And most important thing, you must follow [Discord's Terms of Service](https://discord.com/terms)"
        ))
        container.add_item(ui.Separator())

        container.add_item(ui.TextDisplay(
            'Click **"Select the rule"** to read the rules. They\'re important too.\n'
            'If it gives error **"This interaction failed"** try again.'
        ))
        container.add_item(ui.ActionRow(RuleSelect()))

        container.add_item(ui.TextDisplay("• If someone breaks rules, open a ticket in support."))
        container.add_item(ui.TextDisplay("**Click the buttons below to see re-join info and punishment points.**"))

        point_btn = ui.Button(label="Point Info", style=discord.ButtonStyle.secondary, custom_id="point_info")
        punish_btn = ui.Button(label="Punishment Power", style=discord.ButtonStyle.secondary, custom_id="punishment_power")
        support_btn = ui.Button(label="Support", style=discord.ButtonStyle.link, url="https://discord.gg/kCz3W4VT4")

        point_btn.callback = self.on_point_info
        punish_btn.callback = self.on_punishment

        container.add_item(ui.ActionRow(point_btn, punish_btn, support_btn))

        container.add_item(ui.Separator())
        container.add_item(ui.TextDisplay(
            "*To analyze the unexplained, safeguard the public, and treat those afflicted by "
            "conditions beyond the boundaries of conventional medicine.*"
        ))
        container.add_item(ui.TextDisplay(
            "**Failure to follow these rules will result in disciplinary action**, including warning, "
            "suspension, demotion, or removal from Security depending on the severity of the violation."
        ))
        container.add_item(ui.TextDisplay("-# Made by Saintless"))

        self.add_item(container)

    async def on_point_info(self, interaction: discord.Interaction):
        # Only the person who clicked sees this — ephemeral=True
        await interaction.response.send_message(view=build_reply("Point Info", POINT_INFO), ephemeral=True)

    async def on_punishment(self, interaction: discord.Interaction):
        # Only the person who clicked sees this — ephemeral=True
        await interaction.response.send_message(view=build_reply("Punishment Power", PUNISHMENT_TABLE), ephemeral=True)


# Usage in a command:
# await ctx.send(view=RulesView())

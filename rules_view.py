import discord
from discord import ui

# ─────────────────────────────────────────────────────────────
# COMBINED RULES
#
# This bot is now the single rules bot for:
#   1. General
#   2. Security
#   3. Research
#   4. Technical
#   5. Janitor
# ─────────────────────────────────────────────────────────────

GENERAL_RULES = """꧁ 𓆩✰༺☾ GENERAL RULES ☽༻✰𓆪꧂

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

SECURITY_RULES = """**SECURITY RULES**

**1. WEAPON DISCIPLINE**
• Do not fire without a valid threat.
• No unnecessary firing or mag-dumping.
• Do not shoot personnel because of suspicion alone.
• Do not fire into crowds or populated areas recklessly.
• Keep your weapon under control at all times.

**2. IDENTIFICATION**
• Know who you are dealing with before taking action.
• Do not attack someone simply because they are unfamiliar.
• Ask questions and verify their authorization when appropriate.
• If you are unsure, get a superior rather than immediately escalating.

**3. POST DISCIPLINE**
• Stay at your assigned position unless given permission to leave.
• Do not abandon your post during minor incidents.
• Do not wander around the facility looking for trouble.
• Remain attentive while stationed.

**4. AUTHORITY**
• Follow orders from authorized superiors.
• Do not give orders beyond your rank.
• Do not threaten or intimidate personnel because you have a weapon.
• Security authority must never be used for personal arguments.

**5. RESTRICTED AREAS**
• Do not allow unauthorized personnel into restricted areas.
• Do not enter restricted zones without proper authorization.
• Do not give other players access to areas they are not cleared for.

**6. INCIDENTS**
• Stay calm during emergencies.
• Protect nearby personnel and secure the area.
• Do not make an incident worse through reckless behavior.
• Report serious incidents to the appropriate superior.

**7. PROFESSIONAL CONDUCT**
• No harassment, bullying, or unnecessary aggression.
• Do not randomly detain or attack people.
• Do not start conflicts while on duty.
• Remain professional even when other personnel are being difficult.

**8. ROLEPLAY DISCIPLINE**
• Do not use OOC information for IC decisions.
• Do not randomly kill players for entertainment.
• Follow the facility's RP rules.
• Keep your actions appropriate to your character's position.

**9. EQUIPMENT**
• Do not misuse security equipment.
• Do not take another officer's equipment without permission.
• Report missing or damaged equipment to a superior.

**10. ACCOUNTABILITY**
• Mistakes must be reported instead of hidden.
• Repeated violations will result in disciplinary action.
• Severe misconduct may result in immediate suspension or removal from Security."""

RESEARCH_RULES = """**RESEARCH RULES**

**1. DON'T HARM ANYONE**
• Don't harm anyone in or out this division.

**2. STAY IN YOUR LANE**
• Do your business as a researcher (regardless of high or low rank).
• Each rank is provided their own place and business.

**3. NO HARM DURING ROLEPLAY**
• During roleplay, do NOT murder, harm, assault, make uncomfortable, or guilt trip anyone.
• You're a researcher — not another division with their own tasks and goals.
• Our goal is to find artifacts and discover each specimen.

**4. BE HUMBLE & KIND**
• Be humble and kind to others, avoid assaults and harmful things.
• Do not pick violence against other division personnel.

**5. PINNING MESSAGES**
• Only the High Curator pins messages that are important and need to be seen by other high-ups, including this division (Research Division).

**6. CARE FOR ONE ANOTHER**
• Care for one another, high or low rank, in each division.
• Do not harm or be rude to them — be cautious about what you've done.
• Hesitate before doing something next — think about whether it's right or wrong.

**7. EVIDENCE IS KEPT**
• There are records that will be used to hold you accountable for any assaults you've committed.

**8. YOU'RE BEING WATCHED**
• Not only the High Curator is watching — other higher-ups watch this division's actions toward one another too.

**9. SUSPENSION FOR HARM**
• Suspension and imprisonment are given directly if you have assaulted or harmed any personnel.
• Begging for mercy will not help.

**10. NO FAKE FRIENDLINESS**
• No assumptions, no showing fake friendliness toward others, no using rank as leverage over your name.
• Direct mute or suspension with no hesitation.

**11. DON'T ANNOY HIGH-UPS**
• Don't even think about annoying the High Curator or other high-ups while they're minding their own business.
• They will mark you for suspension."""

TECHNICAL_RULES = """**TECHNICAL RULES**

**1. NO BLAMING OR FRAMING**
• No one will act badly towards others, especially blaming people or framing them.

**2. ACT RESPONSIBLY**
• If you encounter a problem, act accordingly and responsibly.

**3. REACH OUT IF YOU'RE HURTING**
• If you feel hurt or sad and someone is being mean to you, don't worry — you may reach out to me or others.

**4. NO ATTACKING OR HARASSING**
• No attacking people, and no insulting or harassing them.
• Serious consequences follow for anyone who does.

**5. REPRESENT THE DIVISION WELL**
• No acting like a kid — do not embarrass our Technical name, or me.

**6. STAY SERIOUS IN-GAME**
• Act serious in-game. You can be OOC with people you know, and have some fun — just don't take it too far.

**7. DON'T ASK FOR SPECIAL PERMISSION**
• Do not ask for special permission. If you do, I will gladly take this to the higher-ups.

**8. RESPECT THE HIGHER-UPS**
• Do not mess with the higher-ups. If you have a problem, DM me — but only for important matters.

**9. NO METAGAMING / META-GRUDGING**
• Don't metagame or meta-grudge. Learn the proper rules on how to roleplay."""

JANITOR_RULES = """**JANITOR RULES**

**1. ONLY 2 CHANCES**
• You are required to follow the rules strictly — you only get 2 chances if you break them.
• If you break all of them, you will be suspended.

**2. NO MURDER / ASSAULT**
• Don't even think about murdering or assaulting anyone to cause harm, or playing the victim.
• Doing so puts you at high risk of suspension.

**3. EVIDENCE IS KEPT**
• The higher-ups have records and evidence coming from you (low or high rank) to prove you guilty of any charges.

**4. DON'T START FIGHTS**
• Yes, janitors can be dangerous — that doesn't mean you can act like one just to harm others.
• Don't assume you can pick a fight on them — if someone sees you fighting with other personnel, both of you will be reported directly.

**5. ACT YOUR AGE**
• Choose peace and humility instead. Don't act like a kid in front of every player when your character is 18+ and should act like it.

**6. NO ANNOYING OTHER DIVISIONS**
• Don't choose annoyance or anything else against other division personnel.
• The higher-ups are reading your messages and can see the evidence of what, where, and when it happened.

**7. NO FIGHTS, NO VIOLENCE**
• NO picking fights, NO violence, NO harming or annoying other personnel in or out of the division.
• NO giving unexpected reports until the limit is already 10+.
• NO disturbing the higher-ups unless it's actually important.

**8. HIGHER-UPS CAN REACH OUT**
• The higher-ups can read or directly message the division at any time if they see you doing something that isn't clearly right.

**9. THE LIMIT IS 2 — NO EXCEPTIONS**
• You only get 2 chances. No assumptions, no changing that number.
• If you broke them, there's no sympathy for the path you chose.

**10. MIND YOUR OWN BUSINESS**
• All personnel in this division must strictly mind their own business and follow the goals they were given.
• No violence-driven goals, ever.

**11. REPORT, DON'T ENGAGE**
• Resume your own business — do not engage in a fight for someone else's sake.
• Report directly to the Head Janitor instead."""

RULES = {
    "general": GENERAL_RULES,
    "security": SECURITY_RULES,
    "research": RESEARCH_RULES,
    "technical": TECHNICAL_RULES,
    "janitor": JANITOR_RULES,
}

TITLES = {
    "general": "General Rules",
    "security": "Security Rules",
    "research": "Research Rules",
    "technical": "Technical Rules",
    "janitor": "Janitor Rules",
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
    "**Moderate offense** — 3 pts → 24-hour timeout\n"
    "**Serious offense** — 5 pts → 7-day timeout\n"
    "**6+ points total** → 7-day ban\n"
    "**Extreme offense** → Immediate ban\n"
    "**Ban evasion / repeat ban** → **Permanent ban, no excuse**"
)


def build_reply(title: str, body: str, color: discord.Colour = discord.Colour.dark_theme()) -> ui.LayoutView:
    """Build a private Components V2 response for a selected rules category."""
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
            placeholder="Select the rules",
            custom_id="rules_category",
            options=[
                discord.SelectOption(label="General Rules", value="general"),
                discord.SelectOption(label="Security Rules", value="security"),
                discord.SelectOption(label="Research Rules", value="research"),
                discord.SelectOption(label="Technical Rules", value="technical"),
                discord.SelectOption(label="Janitor Rules", value="janitor"),
            ],
        )

    async def callback(self, interaction: discord.Interaction):
        key = self.values[0]
        await interaction.response.send_message(
            view=build_reply(TITLES[key], RULES[key]),
            ephemeral=True,
        )


class RulesView(ui.LayoutView):
    def __init__(self):
        super().__init__(timeout=None)

        container = ui.Container(accent_color=discord.Colour.dark_theme())
        container.add_item(ui.TextDisplay("# Project Heaven — Rules"))
        container.add_item(
            ui.TextDisplay(
                "All department and community rules are now handled by this bot.\n"
                "Select a category below to view the rules."
            )
        )
        container.add_item(ui.Separator())
        container.add_item(
            ui.TextDisplay(
                'Select the rules you want to read. If you get **"This interaction failed"**, '
                "try again or message Saintless."
            )
        )
        container.add_item(ui.ActionRow(RuleSelect()))

        container.add_item(ui.TextDisplay("• If someone breaks rules, open a ticket in support."))
        container.add_item(
            ui.TextDisplay("**Use the buttons below to see re-join info and punishment points.**")
        )

        point_btn = ui.Button(
            label="Point Info",
            style=discord.ButtonStyle.secondary,
            custom_id="point_info",
        )
        punish_btn = ui.Button(
            label="Punishment Power",
            style=discord.ButtonStyle.secondary,
            custom_id="punishment_power",
        )
        support_btn = ui.Button(
            label="Support",
            style=discord.ButtonStyle.link,
            url="https://discord.gg/kCz3W4VT4",
        )

        point_btn.callback = self.on_point_info
        punish_btn.callback = self.on_punishment

        container.add_item(ui.ActionRow(point_btn, punish_btn, support_btn))
        container.add_item(ui.Separator())

        container.add_item(
            ui.TextDisplay(
                "*To analyze the unexplained, safeguard the public, and treat those afflicted by "
                "conditions beyond the boundaries of conventional medicine.*"
            )
        )
        container.add_item(
            ui.TextDisplay(
                "**Failure to follow these rules will result in disciplinary action**, including "
                "warning, suspension, demotion, or removal depending on the severity of the violation."
            )
        )
        container.add_item(ui.TextDisplay("-# Made by Saintless"))

        self.add_item(container)

    async def on_point_info(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            view=build_reply("Point Info", POINT_INFO),
            ephemeral=True,
        )

    async def on_punishment(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            view=build_reply("Punishment Power", PUNISHMENT_TABLE),
            ephemeral=True,
        )

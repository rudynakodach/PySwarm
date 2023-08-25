import pathlib
import datetime
from discord_webhook import DiscordWebhook, DiscordEmbed
from Utils import Utils
import Settings


colors = {
    "yellow": "ffec4f",
    "green": "42b341"
}

def _getWebhook() -> DiscordWebhook:
    return DiscordWebhook(url=Settings.getWebhookUrl())

def hourlyReport(honeySinceStart: int, honeySinceLastHour: int, honeyNow: int, honeyMadeInThisHour: list[dict], timesConverted):
    WEBHOOK = _getWebhook()

    profitSinceStart = honeyNow - honeySinceStart
    hourlyProfit = honeyNow - honeySinceLastHour
    timesConverted = len([convert for convert in honeyMadeInThisHour if convert["fromConverting"]])
    avgHoneyPerConvert = abs(hourlyProfit/timesConverted)
    
    embed = DiscordEmbed()
    # embed.set_timestamp(datetime.datetime.now())
    embed.set_author("PySwarm")
    embed.set_title("Hourly Report")
    embed.set_color(colors["yellow"])

    embed.add_embed_field("Backpacks converted", f"`{timesConverted}`", inline=True)
    embed.add_embed_field("Backpacks per minute", f"1 every `{(3600/timesConverted/60):.2f}` min")
    embed.add_embed_field("Avg. honey per convert", f"`{Utils._formatNumber(avgHoneyPerConvert)}` ({Utils._abbreviateNumber(avgHoneyPerConvert)})", inline=True)

    embed.add_embed_field("Honey made this hour", f"`{Utils._formatNumber(hourlyProfit)}` ({Utils._abbreviateNumber(hourlyProfit)})", inline=True)
    embed.add_embed_field("Profit since start", f"`{Utils._formatNumber(profitSinceStart)}`", inline=True)
    embed.add_embed_field("Avg. honey per minute", f"`{Utils._formatNumber(hourlyProfit/60)}` honey/min", inline=True)


    # embed.add_embed_field()
    WEBHOOK.add_embed(embed)
    if pathlib.Path(pathlib.Path.cwd().as_posix() + "/images/temp/screenshot.png").exists():
        WEBHOOK.add_file(Utils._getScreenshot(), filename="screenshot.png")
    WEBHOOK.execute()

def pollenConverted(lastKnownHoney: int, preConvertHoney: int, postConvertHoney: int):
    WEBHOOK = _getWebhook()

    honeyFromConverting = postConvertHoney - preConvertHoney
    honeyFromLastConvert = preConvertHoney - lastKnownHoney  
    honeyFromLastConvertAfterConverting = postConvertHoney - lastKnownHoney

    embed = DiscordEmbed()

    embed.set_author("PySwarm")
    embed.set_title("Pollen Converted")
    embed.set_color(colors["green"])

    embed.add_embed_field("Honey from converting", f"`{Utils._formatNumber(honeyFromConverting)}` ({Utils._abbreviateNumber(honeyFromConverting)})")
    embed.add_embed_field("Profit since last convert", f"Honey gain on field: `{Utils._formatNumber(honeyFromLastConvert)}` ({Utils._abbreviateNumber(honeyFromLastConvert)})\nHoney from converting: `{Utils._formatNumber(honeyFromLastConvertAfterConverting)}` ({Utils._abbreviateNumber(honeyFromLastConvertAfterConverting)})")
    embed.add_embed_field("Total honey", f"`{Utils._formatNumber(postConvertHoney)}` ({Utils._abbreviateNumber(postConvertHoney)})")

    WEBHOOK.add_embed(embed)
    if pathlib.Path(pathlib.Path.cwd().as_posix() + "/images/temp/screenshot.png").exists():
        WEBHOOK.add_file(Utils._getScreenshot(), "screenshot.png")

    WEBHOOK.execute()
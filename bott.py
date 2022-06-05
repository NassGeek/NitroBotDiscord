import discord
import random
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix = ",", description = "Dev par #5549")

@bot.event
async def on_ready():
    print('bot lancer!')
    activity = discord.Game(name=",aide | bot complètement fr par eldoxx#5549", type=3)
    await bot.change_presence(status=discord.Status.dnd, activity=activity)

@bot.command()
async def nitrogen(ctx):
    print("nitrogenused!")
    nitrocode = ""
    caracteres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in range(3):
        nitrocode = ""
        for i in range(24):
            nitrocode = f"{nitrocode}{random.choice(caracteres)}"
        await ctx.send(f"""https://discord.gift/{nitrocode}
Merci d'utiliser le **iShowSpeed bot** !
*Dev by eldoxx#5549*""")
@bot.command()
async def dire(ctx, *texte):
	await ctx.send(" ".join(texte))

bot.run("YOUR TOKEN")
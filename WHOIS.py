#                  8888888b.   .d8888b.                    d888                     
#                  888  "Y88b d88P  Y88b                  d8888                     
#                  888    888      .d88P                    888                     
#888  888  .d88b.  888    888     8888"  888d888 88888b.    888   88888b.   8888b.  
#`Y8bd8P' d88""88b 888    888      "Y8b. 888P"   888 "88b   888   888 "88b     "88b 
#  X88K   888  888 888    888 888    888 888     888  888   888   888  888 .d888888 
#.d8""8b. Y88..88P 888  .d88P Y88b  d88P 888     888 d88P   888   888  888 888  888 
#888  888  "Y88P"  8888888P"   "Y8888P"  888     88888P"  8888888 888  888 "Y888888 
#                                                888                                
#                                                888                                
#                                                888                                
#
#   https://linktr.ee/strikesec

import discord
from discord.ext import commands
import requests

class WHOIS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='WHOIS')
    async def search(self, ctx):
        if ctx.channel.id != YOUR-CHANNEL-ID:  # Check if the command is used in channel #1337
            return await ctx.send("This command can only be used in the testing discord channel.")

        url = "YOUR-API-URL"
        querystring = {"domain": "API-URL"}
        headers = {
            "x-rapidapi-key": "YOUR-API-KEY",
            "x-rapidapi-host": "YOUR-API-HOST"
        }
        response = requests.get(url, headers=headers, params=querystring)
        result = response.json()

        await ctx.send(result)

async def setup(bot):
    await bot.add_cog(WHOIS(bot))

import logging
import discord
import aiohttp

from discord.ext import commands
from discord import app_commands
from Utils import WeatherUtils
from Utils import ImageUtils
from Utils import EmbedColourUtils

class weather(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    

    weather = app_commands.Group(name="weather",description="Real Life Weather Search Commands.")

    @weather.command(name="location",description="Looks up real time weather data for a specific location")
    @app_commands.describe(
        location = "The location that you want to search for"
    )
    async def weatherlookup(self,interaction: discord.Interaction,location:str):
        await interaction.response.defer(thinking=True)

        #converting our location into geo coordinates
        loc = await WeatherUtils.geoconv(location=location)
        lat= loc.latitude
        long =loc.longitude

        #calling the api with the coordinates
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current_weather=True') as r:
                json = await r.json()
        
        #getting the date out of the json here
        gentime= json["generationtime_ms"]
        temp= json["current_weather"]["temperature"] #C    
        windspeed= json["current_weather"]["windspeed"]
        winddirection= json["current_weather"]["winddirection"]#degrees
        wwcode = json["current_weather"]["weathercode"]

        #getting our pic from our code!
        img_name=await ImageUtils.getpic(wwcode)
        f= discord.File(f"Imgs//assets//{img_name}",filename=img_name)

        #getting our embed colour
        colour = await EmbedColourUtils.getColour(wwcode)

        #getting the weathertype
        weathertype =await WeatherUtils.checkcode(wwcode)

        #making that CLEAN AS HELL EMBED

        embed = discord.Embed(title=f"Location: `{location.capitalize()}`",description=f"**The weather forecast is `{weathertype}`**.\n\n**{temp}°C** **Wind: {windspeed}km/h ({winddirection}°**).",colour=colour)
        embed.set_thumbnail(url=f"attachment://{img_name}")
        embed.set_footer(text=f"Powered-by: open-meteo.com |Took {round(gentime,2)}ms")
        
        #sending the embed and the file aka our img
        await interaction.followup.send(embed=embed,file=f)




async def setup(bot: commands.Bot):
    await bot.add_cog(weather(bot))
from geopy import Nominatim

async def geoconv(location:str):
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode(location)
    
    return getLoc

#WMO Weather interpretation codes. This gets returned in the response json from the api. We just format it here to be 'normal' human-readable
async def checkcode(code:int) -> str:
    if code  == 0:
        return("Clear")
    elif code == 1:
        return("Mainly Clear")
    elif code == 2:
        return("Partly Cloudy")
    elif code == 3:
        return("Overcast Cloudy")
    elif code == 45:
        return("Fog")
    elif code == 48:
        return("Depositing rime frog")
    elif code == 51:
        return("Light Drizzle")
    elif code == 53:
        return("Moderate Drizzle")
    elif code == 55:
        return("Dense Drizzle")
    elif code == 56:
        return("Light Freezing Drizzle")
    elif code == 57:
        return("Dense Freezing Drizzle")
    elif code == 61:
        return("Slight Rain")
    elif code == 63:
        return("Moderate Rain")
    elif code == 65:
        return("Heavy Rain")
    elif code == 66:
        return("Light Freezing Rain")
    elif code == 67:
        return("Heavy Freezing Rain")
    elif code == 71:
        return("Slight Snow-fall")
    elif code == 73:
        return("Moderate Snow-fall")
    elif code == 75:
        return("Heavy Snow-fall")
    elif code == 77:
        return("Snow Grains")
    elif code == 80:
        return("Slight Rain showers")
    elif code == 81:
        return("Moderate Rain showers")
    elif code == 82:
        return("Violent Rain showers")
    elif code == 85:
        return("Slight Snow showers")
    elif code == 86:
        return("Heavy Snow showers")
    elif code == 95:
        return("Thunderstorm")
    elif code == 96:
        return("Thunderstorm with slight hail")
    elif code == 99:
        return("Tunderstorm with heavy hail")


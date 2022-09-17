#https://content.meteoblue.com/en/specifications/standards/symbols-and-pictograms for the imagesscroll to the bottom for the zip containing them

async def getpic(code:int) -> str:
    if code  == 0:
        return("clear.png")
    elif code == 1:
        return("MainlyClear.png")
    elif code == 2:
        return("PartlyCloudy.png")
    elif code == 3:
        return("OvercastCloudy.png")
    elif code == 45:
        return("Fog.png")
    elif code == 48:
        return("Depositingrimefrog.png")
    elif code == 51:
        return("LightDrizzle.png")
    elif code == 53:
        return("ModerateDrizzle.png")
    elif code == 55:
        return("DenseDrizzle.png")
    elif code == 56:
        return("LightFreezingDrizzle.png")
    elif code == 57:
        return("LightFreezingDrizzle.png")
    elif code == 61:
        return("LightDrizzle.png")
    elif code == 63:
        return("ModerateDrizzle.png")
    elif code == 65:
        return("DenseDrizzle.png")
    elif code == 66:
        return("LightFreezingDrizzle.png")
    elif code == 67:
        return("LightFreezingDrizzle.png")
    elif code == 71:
        return("SlightSnowfall.png")
    elif code == 73:
        return("ModerateSnowfall.png")
    elif code == 75:
        return("HeavySnowfall.png")
    elif code == 77:
        return("LightFreezingDrizzle.png")
    elif code == 80:
        return("LightDrizzle.png")
    elif code == 81:
        return("ModerateDrizzle.png")
    elif code == 82:
        return("DenseDrizzle.png")
    elif code == 85:
        return("SlightSnowfall.png")
    elif code == 86:
        return("HeavySnowfall.png")
    elif code == 95:
        return("Thunderstorm.png")
    elif code == 96:
        return("Thunderstorm.png")
    elif code == 99:
        return("Thunderstorm.png")



#returns the colour code per ww code 
async def getColour(code:int):
    if code  == 0:
        return 0xf1c40f
    elif code == 1:
        return 0xf1c40f
    elif code == 2:
        return 0xf1c40f
    elif code == 3:
        return 0xf1c40f
    elif code == 45:
        return 0x546e7a
    elif code == 48:
        return 0x979c9f
    elif code == 51:
        return 0x3498db
    elif code == 53:
        return 0x3498db
    elif code == 55:
        return 0x3498db
    elif code == 56:
        return 0x3498db
    elif code == 57:
        return 0x3498db
    elif code == 61:
        return 0x7289da
    elif code == 63:
        return 0x7289da
    elif code == 65:
        return 0x7289da
    elif code == 66:
        return 0x7289da
    elif code == 67:
        return 0x7289da
    elif code == 71:
        return 0x95a5a6
    elif code == 73:
        return 0x95a5a6
    elif code == 75:
        return 0x95a5a6
    elif code == 77:
        return 0x95a5a6
    elif code == 80:
        return 0x7289da
    elif code == 81:
        return 0x7289da
    elif code == 82:
        return 0x7289da
    elif code == 85:
        return 0x95a5a6
    elif code == 86:
        return 0x95a5a6
    elif code == 95:
        return 0x992d22
    elif code == 96:
        return 0x992d22
    elif code == 99:
        return 0x992d22

#yoinked from https://stackoverflow.com/questions/63768372/color-codes-for-discord-py
class colours():
    default = 0
    teal = 0x1abc9c
    dark_teal = 0x11806a
    green = 0x2ecc71
    dark_green = 0x1f8b4c
    blue = 0x3498db
    dark_blue = 0x206694
    purple = 0x9b59b6
    dark_purple = 0x71368a
    magenta = 0xe91e63
    dark_magenta = 0xad1457
    gold = 0xf1c40f
    dark_gold = 0xc27c0e
    orange = 0xe67e22
    dark_orange = 0xa84300
    red = 0xe74c3c
    dark_red = 0x992d22
    lighter_grey = 0x95a5a6
    dark_grey = 0x607d8b
    light_grey = 0x979c9f
    darker_grey = 0x546e7a
    blurple = 0x7289da
    greyple = 0x99aab5

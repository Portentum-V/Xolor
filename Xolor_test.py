"""
    Xolor tests
"""

from Xolor import Xolor

def color_test():
    xolor = Xolor()
    print(xolor.color_str(xolor.RUBY, "Ruby"))
    print(xolor.color_str(xolor.EMERALD, "Emerald"))
    print(xolor.color_str(xolor.ORANGE, "Orange"))
    print(xolor.color_str(xolor.SAPPHIRE, "Sapphire"))
    print(xolor.color_str(xolor.PURPLE, "Purple"))
    print(xolor.color_str(xolor.AQUA, "Aqua"))
    print(xolor.color_str(xolor.SILVER, "Silver"))
    print(xolor.color_str(xolor.BG_BLACK, "Silver on Black"))
    print(xolor.color_str(xolor.BG_RUBY, "BG Ruby"))
    print(xolor.color_str(xolor.BG_EMERALD, "BG Emerald")) 
    print(xolor.color_str(xolor.BG_ORANGE, "BG Orange"))
    print(xolor.color_str(xolor.BG_SAPPHIRE, "BG Sapphire"))
    print(xolor.color_str(xolor.BG_PURPLE, "BG Purple"))
    print(xolor.color_str(xolor.BG_AQUA, "BG Aqua"))
    print(xolor.color_str(xolor.BG_SILVER, f"{xolor.BLACK}FG Black on BG Silver"))
    print(xolor.color_str(xolor.GRAY, "Gray"))
    print(xolor.color_str(xolor.RED, "Red"))
    print(xolor.color_str(xolor.GREEN, "Green"))  
    print(xolor.color_str(xolor.YELLOW, "Yellow"))
    print(xolor.color_str(xolor.BLUE, "Blue"))
    print(xolor.color_str(xolor.MAGENTA, "Magenta"))
    print(xolor.color_str(xolor.CYAN, "Cyan"))
    print(xolor.color_str(xolor.WHITE, "White"))
    print(xolor.color_str(xolor.BG_GRAY, "BG Gray"))
    print(xolor.color_str(xolor.BG_RED, "BG Red"))
    print(xolor.color_str(xolor.BG_GREEN, "BG Green"))
    print(xolor.color_str(xolor.BG_YELLOW, "BG Yellow"))
    print(xolor.color_str(xolor.BG_BLUE, "BG Blue"))
    print(xolor.color_str(xolor.BG_MAGENTA, "BG Magenta"))
    print(xolor.color_str(xolor.BG_CYAN, "BG Cyan"))
    print(xolor.color_str(xolor.BG_WHITE, "BG White"))
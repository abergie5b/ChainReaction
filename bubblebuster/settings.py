
# DEBUG
DEBUG = True

# VERSION
VERSION = 0.001


class InterfaceSettings:
    DARKMODE = False

    # DISPLAY SETTINGS
    if DEBUG: # windowed
        SCREEN_WIDTH = 1024
        SCREEN_HEIGHT = 768
    else:
        SCREEN_WIDTH = 0 # fullscreen
        SCREEN_HEIGHT = 0
        
    BACKGROUND_COLOR = (0, 0, 0)
    BACKGROUND_COLOR_LIGHT = (200, 200, 200)

    # FONT SETTINGS
    MOUSEHIGHLIGHTFONTCOLOR = (255, 255, 255)
    MOUSEHIGHLIGHTFONTCOLOR_LIGHT = (225, 225, 225)

    FONTTITLECOLOR = (255, 255, 255)
    FONTTITLECOLOR_LIGHT = (0, 0, 0)

    FONTCOLOR = (205, 205, 205)
    FONTCOLOR_LIGHT = (50, 50, 50)

    FONTSTYLE = 'resources/GFSCUS1D.ttf'

    # BUBBLES
    BUBBLECOLORS = ['blue', 'cyan', 'green', 'orange', 'pink']

    # EXPLOSION
    EXPLOSIONCOLOR = (165, 0, 0)


# BUBBLE SETTINGS
NUMBER_OF_BUBBLES = 25
BUBBLE_MAXH = 250
BUBBLEPOPDELAY = 500
BUBBLE_MAXDELTA = 100


class GameSettings:
    # i dont like dis
    # is this needed anymore?
    @staticmethod
    def init():
        # BUBBLE SETTINGS
        GameSettings.NUMBER_OF_BUBBLES = NUMBER_OF_BUBBLES
        GameSettings.BUBBLE_MAXH = BUBBLE_MAXH
        GameSettings.BUBBLEPOPDELAY = BUBBLEPOPDELAY
        GameSettings.BUBBLE_MAXDELTA = BUBBLE_MAXDELTA


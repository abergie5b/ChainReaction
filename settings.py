
# DEBUG
DEBUG = True

# DISPLAY SETTINGS
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800


# BUBBLE SETTINGS
NUMBER_OF_BUBBLES = 10
BUBBLE_MAXH = 200
BUBBLEPOPDELAY = 500

# PLAYER SETTINGS
PLAYER_EXPLOSIONS = 10
PLAYER_LIVES = 3

# EXPLOSION SETTINGS
EXPLOSION_MAX_LIVES = 25
EXPLOSION_RADIUS = 10 
EXPLOSION_RADIUS_DELTA = 5

SMALLEXPLOSIONCOST = 1
LARGEEXPLOSIONCOST = 2


class InterfaceSettings:
    MOUSEHIGHLIGHTFONTCOLOR = (255, 255, 255)
    FONTTITLECOLOR = (225, 225, 225)
    FONTCOLOR = (215, 215, 215)
    FONTSTYLE = 'resources/GFSCUS1D.ttf'


class GameSettings:
    @staticmethod
    def init():
        # BUBBLE SETTINGS
        GameSettings.NUMBER_OF_BUBBLES = NUMBER_OF_BUBBLES
        GameSettings.BUBBLE_MAXH = BUBBLE_MAXH
        GameSettings.BUBBLEPOPDELAY = BUBBLEPOPDELAY

        # PLAYER SETTINGS
        GameSettings.PLAYER_EXPLOSIONS = PLAYER_EXPLOSIONS
        GameSettings.PLAYER_LIVES = PLAYER_LIVES

        # EXPLOSION SETTINGS
        GameSettings.EXPLOSION_MAX_LIVES = EXPLOSION_MAX_LIVES
        GameSettings.EXPLOSION_RADIUS = EXPLOSION_RADIUS
        GameSettings.EXPLOSION_RADIUS_DELTA = EXPLOSION_RADIUS_DELTA

        GameSettings.SMALLEXPLOSIONCOST = SMALLEXPLOSIONCOST
        GameSettings.LARGEEXPLOSIONCOST = LARGEEXPLOSIONCOST

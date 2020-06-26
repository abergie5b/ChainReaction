import pygame

from bubblebuster.scene import SceneContext
from bubblebuster.settings import SCREEN_HEIGHT, SCREEN_WIDTH, GameSettings, InterfaceSettings

class Game:
    def __init__(self):
        # required for pygame
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 
                                               flags=pygame.RESIZABLE)
        self.running = True
        self.FPS = 90

        GameSettings.init()
        self.scene_context = SceneContext(self)

    def draw(self):
        self.scene_context.scene_state.draw()

        # draw the entire screen
        pygame.display.update()

        # clear the display
        # is there ... a better way? -.-
        self.screen.fill(InterfaceSettings.BACKGROUND_COLOR)

    def update(self):
        self.scene_context.scene_state.update()

    def run(self):

        # Fill the background with black
        self.scene_context.scene_state.screen.fill(InterfaceSettings.BACKGROUND_COLOR)

        # get clock for FPS
        clock = pygame.time.Clock()

        # main event loop
        while self.running:

            # update objects
            self.update()

            # draw objects
            self.draw()

            # tick tock
            clock.tick(self.FPS)

        # quit
        pygame.quit()


if __name__ == '__main__':
    Game().run()


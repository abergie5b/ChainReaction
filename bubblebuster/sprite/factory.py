import bubblebuster.sprite as sp
from bubblebuster.settings import InterfaceSettings
from bubblebuster.image import ImageNames, ImageMan

from random import randint, choice


class CircleFactory:
    def __init__(self, group, manager):
        self.group = group
        self.manager = manager

    def generate_random(self, number_of_circles, max_xy=(800, 600), max_h=120, alpha=255):
            maxx, maxy = max_xy
            for x in range(number_of_circles):
                w, h = (1, randint(max_h//6, max_h))
                posxy = (randint(h//2, maxx-h-5), randint(h//2, maxy-h-5))
                bubble = choice(InterfaceSettings.BUBBLECOLORS).upper()
                image = ImageMan.instance.find(getattr(ImageNames, '%sBUBBLE' % bubble))
                self.create_circle(image, posxy, (w, h), self.get_random_color(alpha), alpha=alpha)

    def get_random_color(self, alpha=None):
        r = randint(75, 200)
        g = randint(75, 225)
        b = randint(75, 225)
        if alpha:
            return (r, g, b, alpha)
        return (r, g, b)

    def create_circle(self, image, posxy, wh, color, alpha=255):
        x, y = posxy
        w, h = wh
        sprite = sp.CircleSprite(sp.BoxSpriteNames.CIRCLE, image, w, h, x, y, color=color, alpha=alpha)
        self.manager.add_sprite(sprite)
        self.group.add(sprite)

from constants import SPRITE_SHEETS, WHITE
from pyglet.image import load


class SpriteSheet:

    def __init__(self, filename):
        """Load the sheet."""
        self.sheet = load (SPRITE_SHEETS + filename)

    def image_at(self, *rectangle):
        return self.sheet.get_region (*rectangle)


def load_sheets():
    ret = {}

    comp = SpriteSheet ('complete.png')

    count = 0

    for i in range (32):
        for j in range (64):
            ret[count] = comp.image_at (j * 32, (31 - i) * 32, 32, 32)
            count += 1

    # for i in range (16):
    #     for j in range (16):
    #         ret[count] = plants.image_at ((j * 32, i * 32, 32, 32))
    #         count += 1

    return ret

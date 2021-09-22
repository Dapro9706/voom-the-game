import pyglet
from pyglet.gl import glClearColor
from spritesheet import load_sheets
from constants import Wn, Hn
from map import load_map


class Window (pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super ().__init__ (*args, **kwargs)
        self.set_minimum_size (args[0], args[1])
        background_color = [255, 255, 255, 255]
        background_color = [i / 255 for i in background_color]
        glClearColor (*background_color)

        self.sprites = load_sheets ()

        self.batch = pyglet.graphics.Batch ()
        self.current_map = load_map ('test_map')

    def on_key_press(self, symbol, modifiers):
        pass

    def on_key_release(self, symbol, modifiers):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_draw(self):
        self.clear ()
        buffer = []

        for i in range (Wn):
            for j in range (Hn):
                sp_ref = int (self.current_map['Ground'][j][i])

                if sp_ref != -1:
                    buffer.append (
                        pyglet.sprite.Sprite (self.sprites[sp_ref], x=i * 32,
                                              y=(Hn - 1 - j) * 32, batch=self.batch)
                    )

        self.batch.draw ()

        buffer = []

        for i in range (Wn):
            for j in range (Hn):
                sp_ref = int (self.current_map['Ground_props'][j][i])
                if sp_ref != -1:
                    buffer.append (
                        pyglet.sprite.Sprite (self.sprites[sp_ref], x=i * 32,
                                              y=(Hn - 1 - j) * 32, batch=self.batch)
                    )

        self.batch.draw()

    def update(self, dt, dx):
        pass

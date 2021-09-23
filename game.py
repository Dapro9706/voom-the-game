import pyglet
from pyglet.gl import glClearColor
from spritesheet import load_sheets
from constants import Wn, Hn, WALK_CONST
from map import load_map
from player import Player
from time import sleep


class Window (pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super ().__init__ (*args, **kwargs)
        self.set_minimum_size (args[0], args[1])
        background_color = [255, 255, 255, 255]
        background_color = [i / 255 for i in background_color]
        glClearColor (*background_color)

        # self.tasks = []

        self.sprites = load_sheets ()
        self.player = Player ()

        self.walk_flag = [False, (), 0]

        self.batch = pyglet.graphics.Batch ()
        self.current_map = load_map ('test_map')

    def on_key_press(self, symbol, modifiers):

        walk_unit = .5

        try:
            walk = tuple (map (lambda e: e * walk_unit, WALK_CONST[symbol]))
            self.walk_flag = [True, walk, (self.walk_flag[2] + 1) % 2]
            self.player.move (*walk)
        except KeyError:
            pass

    def on_key_release(self, symbol, modifiers):
        if symbol in [119, 115, 100, 97]:

            def check_dec(a):
                return (a - int (a)) > 0

            x = self.player.rect['x']
            y = self.player.rect['y']

            if check_dec(x) or check_dec(y):
                self.player.move (*self.walk_flag[1])
                self.walk_flag = [False, (), 0]

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_draw(self):
        self.clear ()
        buffer = []


        # itr = 0
        # while itr in range (len (self.tasks)):
        #     if self.tasks[itr].run () == -1:
        #         del self.tasks[itr]
        #         itr -= 1
        #     itr += 1

        if self.walk_flag[0]:
            self.player.move (*self.walk_flag[1])

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

        buffer.append (
            pyglet.sprite.Sprite (self.sprites[597], **self.player.pre_render (), batch=self.batch)
        )

        self.batch.draw ()

    def update(self, dt, dx):
        pass

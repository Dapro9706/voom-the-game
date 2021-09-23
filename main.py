from game import Window, pyglet

frameRate = 60

if __name__ == '__main__':
    win = Window (768, 512, "Test")
    pyglet.clock.schedule (win.update, 1 / frameRate)
    pyglet.app.run ()

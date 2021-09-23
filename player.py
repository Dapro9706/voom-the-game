class Player:
    def __init__(self):
        self.rect = {'x': 0, 'y': 0}

    def move(self, x, y):
        self.rect['x'] += x
        self.rect['y'] += y

    def pre_render(self):
        return {
            'x': self.rect['x'] * 32,
            'y': self.rect['y'] * 32
        }

MAP_PATH = 'data/maps/'
SPRITE_SHEETS = 'data/sprite_sheets/'
MAP_LAYERS = [
    'Ground',
    'Ground_props'
]

W, H, Wn, Hn = (768, 512, 24, 16)

WHITE = (255, 255, 255)
WALK_CONST = {
    119: (0, 1),
    115: (0, -1),
    100: (1, 0),
    97: (-1, 0),
}

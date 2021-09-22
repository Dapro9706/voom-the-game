from constants import MAP_PATH, MAP_LAYERS
import csv


def load_map(new_map):
    return Map (new_map)


class Map:
    def __init__(self, map_name):
        self.layers = {}
        for i in MAP_LAYERS:
            with open (f'{MAP_PATH + map_name}/{map_name}_{i}.csv') as f:
                self.layers[i] = list (csv.reader (f))

    def __getitem__(self, item):
        return self.layers[item]

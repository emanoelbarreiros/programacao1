import pyxel

#cell types
CELL_A = (16,0)
CELL_B = (24,0)
CELL_C = (16,8)
CELL_D = (24,8)
CELL_E = (32,0)
CELL_F = (32,8)
CELL_G = (40,0)
CELL_H = (48,0)
CELL_I = (40,8)
CELL_J = (48,8)
CELL_K = (0,16)
CELL_L = (8,16)
CELL_M = (0,24)
CELL_N = (8,24)
CELL_O = (16,16)
CELL_P = (24,16)
CELL_Q = (16,24)
CELL_R = (24,24)
CELL_S = (32,16)
CELL_T = (40,16)
CELL_U = (32,24)
CELL_V = (40,24)
CELL_EMPTY = (56,0)
CELL_FOOD = (56,8)
CELL_POWER = (56,16)
CELL_DOOR = (48,16)

CELL_TYPES = {
    'A': CELL_A,
    'B': CELL_B,
    'C': CELL_C,
    'D': CELL_D,
    'E': CELL_E,
    'F': CELL_F,
    'G': CELL_G,
    'H': CELL_H,
    'I': CELL_I,
    'J': CELL_J,
    'K': CELL_K,
    'L': CELL_L,
    'M': CELL_M,
    'N': CELL_N,
    'O': CELL_O,
    'P': CELL_P,
    'Q': CELL_Q,
    'R': CELL_R,
    'S': CELL_S,
    'T': CELL_T,
    'U': CELL_U,
    'V': CELL_V,
    '0': CELL_EMPTY,
    '1': CELL_FOOD,
    '2': CELL_POWER,
    '3': CELL_DOOR

}

#BLINKY #red
#PINKY #pink
#INKY #light blue
#SUE #orange


class GameMap:
    def __init__(self, definition, top_offset):
        self.definition = definition
        self.tile_size = 8
        self.top_offset = top_offset

    def draw(self):
        for i, line in enumerate(self.definition):
            for j, c in enumerate(line):
                cell = CELL_TYPES[c]
                pyxel.blt(j * 8, self.top_offset + i * 8, 0, cell[0], cell[1], self.tile_size, self.tile_size, 0)


class Player:
    def __init__(self, position, character_type):
        self.position = position

class Ghost:
    def __init__(self, position, ghost_type):
        self.position = position
        self.ghost_type = ghost_type

class Game:
    def __init__(self):
        pyxel.init(184, 200)
        pyxel.load('pacman.pyxel')
        #read map data from file
        with open('map1.txt') as f:
            map_data = f.readlines()
        map_data = [l.strip() for l in map_data]
        self.game_map = GameMap(map_data, 20)
        self.is_map_drawn = False

        #never put code after this line, it will not be executed
        pyxel.run(self.update, self.draw)

    def update(self):
        pass
    
    def draw(self):
        if not self.is_map_drawn:
            self.game_map.draw()

Game()
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

class GameMap:
    def __init__(self, game_control, definition, top_offset):
        self.definition = []
        self.game_control = game_control
        self.transport_tiles = {}
        for line in definition:
            if line.startswith('.'):
                line = line[1:].split('<>')
                cell1 = eval(line[0])
                cell2 = eval(line[1])
                self.transport_tiles[cell1] = cell2
                self.transport_tiles[cell2] = cell1
            else:
                self.definition.append(line)
        self.tile_size = 8
        self.top_offset = top_offset

    def draw(self, shake_x, shake_y):
        for i, line in enumerate(self.definition):
            for j, c in enumerate(line):
                cell = CELL_TYPES[c]
                pyxel.blt(j * 8 + shake_x, self.top_offset + i * 8 + shake_y, 0, cell[0], cell[1], self.tile_size, self.tile_size, 0)

    def is_player_allowed(self, tile):
        if tile:
            #the cell is empty or has food or has power pill
            line, column = tile
            allowed = False
            if line >= 0 and line <= len(self.definition) - 1 and column >= 0 and column <= len(self.definition[0]) - 1:
                allowed = self.definition[line][column] == '0' or self.definition[line][column] == '1' or self.definition[line][column] == '2'
            return allowed or self.is_transport_tile(tile)
        else:
            return False

    def is_transport_tile(self, tile):
        return tile in self.transport_tiles

    def get_transport_destination(self, tile):
        return self.transport_tiles[tile]

    def eat_food(self, line, column):
        if not self.is_transport_tile((line,column)):
            if self.definition[line][column] == '2':
                self.game_control.shake = 4

            if self.definition[line][column] == '1'or self.definition[line][column] == '2': #food or power
                self.definition[line] = self.definition[line][:column] + '0' + self.definition[line][column + 1:]
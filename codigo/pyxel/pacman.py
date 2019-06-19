import pyxel


#character state
STOPPED = 0
WALKING = 1


#character orientation
RIGHT = 0
LEFT = 1
DOWN = 2
UP = 3
AWAY = 4

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

    def is_player_allowed(self, tile):
        if tile:
            #the cell is empty or has food or has power
            line, column = tile
            allowed = self.definition[line][column] == '0' or self.definition[line][column] == '1' or self.definition[line][column] == '2'
            return allowed
        else:
            return False

    def eat_food(self, line, column):
        if self.definition[line][column] == '1'or self.definition[line][column] == '2': #food or power
            self.definition[line] = self.definition[line][:column] + '0' + self.definition[line][column + 1:]

class Player:
    def __init__(self, tile, current_direction, top_offset, game_map):
        self.intended_direction = current_direction
        self.current_direction = current_direction
        self.state = STOPPED
        self.top_offset = top_offset
        self.tile = tile
        self.speed = 1
        self.game_map = game_map
        self.steps_per_tile = self.game_map.tile_size // self.speed
        self.steps = {
            RIGHT: [(self.speed,0)]*self.steps_per_tile,
            LEFT: [(-self.speed,0)]*self.steps_per_tile,
            UP: [(0,-self.speed)]*self.steps_per_tile,
            DOWN: [(0,self.speed)]*self.steps_per_tile
        }
        self.absolute_position = (self.tile[1]*8, self.tile[0]*8 + self.top_offset)
        self.current_animation_frame = 0
        self.move_buffer = []
        self.animation_frames = [
            [(0,32),(8,32),(0,40),(8,40)],    #right
            [(0,32),(32,32),(24,40),(32,40)], #left
            [(0,32),(40,32),(48,32),(40,40)], #down
            [(0,32),(16,32),(24,32),(16,40)], #up
            [(0,32),(0,32),(0,32),(0,32)]  #away
        ]

    def get_current_tile(self):
        tile = ((self.absolute_position[1] - self.top_offset) // 8, self.absolute_position[0] // 8)
        return tile

    def opposites(self, dir1, dir2):
        are_opposites = (dir1 == UP and dir2 == DOWN) or (dir1 == DOWN and dir2 == UP) or (dir1 == LEFT and dir2 == RIGHT) or (dir1 == RIGHT and dir2 == LEFT)
        return are_opposites

    def handle_movement(self):
        move = None
        if self.opposites(self.intended_direction, self.current_direction):
            count = len(self.move_buffer)
            self.move_buffer.clear() #clear the move buffer
            self.move_buffer.extend(self.steps[self.intended_direction][:self.steps_per_tile - count]) #make the character return to the tile base position
            self.current_direction = self.intended_direction

        if len(self.move_buffer) == 0: #will try to move to the next tile
            #calculate tile the character is at, based on absolute position
            line, column = self.get_current_tile()
            intended_tile = None
            steps = None
            #calculate the tile the character wants to go to
            if self.intended_direction == UP:
                intended_tile = (line - 1, column)
            elif self.intended_direction == DOWN:
                intended_tile = (line + 1, column)
            elif self.intended_direction == LEFT:
                intended_tile = (line, column - 1)
            elif self.intended_direction == RIGHT:
                intended_tile = (line, column + 1)

            if self.game_map.is_player_allowed(intended_tile): #if player is allowed to move based on the intended direction
                self.current_direction = self.intended_direction
                self.move_buffer.extend(self.steps[self.current_direction])
                move = self.move_buffer.pop(0)
            else: #else, try to move based on the old direction
                if self.current_direction == UP:
                    intended_tile = (line - 1, column)
                elif self.current_direction == DOWN:
                    intended_tile = (line + 1, column)
                elif self.current_direction == LEFT:
                    intended_tile = (line, column - 1)
                elif self.current_direction == RIGHT:
                    intended_tile = (line, column + 1)

                if self.game_map.is_player_allowed(intended_tile): #if allowed to move using the old direction
                    self.move_buffer.extend(self.steps[self.current_direction])
                    move = self.move_buffer.pop(0)

        else:
            move = self.move_buffer.pop(0)

        if move:
            self.absolute_position = (self.absolute_position[0] + move[0], self.absolute_position[1] + move[1])

    def handle_food(self):
        tile = self.get_current_tile()
        base_tile_position = (tile[1]*self.game_map.tile_size, tile[0]*self.game_map.tile_size + self.top_offset)
        if self.absolute_position == base_tile_position:
            self.game_map.eat_food(*tile)

    def update(self):
        self.handle_movement()
        self.handle_food()

    def draw(self):
        if pyxel.frame_count % 3 == 0 and self.state == WALKING:
            self.current_animation_frame = (self.current_animation_frame + 1) % 4

        pyxel.blt(self.absolute_position[0], self.absolute_position[1], 0, 
            self.animation_frames[self.current_direction][self.current_animation_frame][0], 
            self.animation_frames[self.current_direction][self.current_animation_frame][1], 
            8, 8, 0)
            

class Ghost:
    def __init__(self, position, ghost_type):
        self.position = position
        self.ghost_type = ghost_type

class Game:
    def __init__(self):
        pyxel.init(184, 210, fps=60)
        pyxel.load('pacman.pyxel')
        self.top_offset = 20
        #read map data from file
        with open('map1.txt') as f:
            map_data = f.readlines()
        map_data = [l.strip() for l in map_data]
        self.game_map = GameMap(map_data, self.top_offset)
        self.intended_direction = AWAY
        self.player_tile = (12,11)
        self.player = Player(self.player_tile, self.intended_direction, self.top_offset, self.game_map)
        #never put code after this line, it will not be executed
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.intended_direction = LEFT
            self.player.state = WALKING
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.intended_direction = RIGHT
            self.player.state = WALKING
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.intended_direction = DOWN
            self.player.state = WALKING
        elif pyxel.btn(pyxel.KEY_UP):
            self.intended_direction = UP
            self.player.state = WALKING
        
        self.player.intended_direction = self.intended_direction
        self.player.update()
    
    def draw(self):
        pyxel.cls(0)
        self.game_map.draw()
        self.player.draw()

Game()
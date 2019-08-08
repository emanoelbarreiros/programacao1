import pyxel
import math

BLINKY = 0
PINKY = 1
INKY = 2
CLYDE = 3

RIGHT = 0
LEFT = 1
DOWN = 2
UP = 3

NO_UP_TILES = {(8,10), (8,12),(16,10),(16,12)}

IN_HOUSE = 0
INIT = 1
CHASE = 2
SCATTER = 3

#modes per level (mode, duration in frames)
LEVEL_1_MODES = [(SCATTER,210),(CHASE,600),(SCATTER,210),(CHASE,600),(SCATTER,150),(CHASE,600),(SCATTER,150),(CHASE,-1)]
LEVEL_2TO4_MODES = [(SCATTER,210),(CHASE,600),(SCATTER,210),(CHASE,600),(SCATTER,150),(CHASE,30990),(SCATTER,1),(CHASE,-1)]
LEVEL_5TOEND_MODES = [(SCATTER,150),(CHASE,600),(SCATTER,150),(CHASE,600),(SCATTER,150),(CHASE,31110),(SCATTER,1),(CHASE,-1)]

IMEDIATE = 0
CONDITION_FOOD_LEFT
TIME
(action,when,how_long)

class Ghost:
    def __init__(self, speed, game_map, top_offset, tile, persona, level):
        self.persona = persona
        self.home_tiles = [(-3, 20), (-3, -2), (23, 22), (23,0)] #[blinky, pinky, inky, clyde]
        self.animation_frames = [
            [[(0,64), (8,64)],[(16,64), (24,64)],[(32,64), (40,64)],[(48,64), (56,64)]], #blinky
            [[(0,48), (8,48)],[(16,48), (24,48)],[(32,48), (40,48)],[(48,48), (56,48)]], #pinky
            [[(0,56), (8,56)],[(16,56), (24,56)],[(32,56), (40,56)],[(48,56), (56,56)]], #inky
            [[(0,72), (8,72)],[(16,72), (24,72)],[(32,72), (40,72)],[(48,72), (56,72)]]  #clyde
        ]
        self.game_map = game_map
        self.speed = speed
        self.steps_per_tile = self.game_map.tile_size // self.speed
        self.current_tile = tile
        self.top_offset = top_offset
        self.absolute_position = (self.tile[1]*8, self.tile[0]*8 + self.top_offset)
        self.current_animation_frame = 0
        self.move_buffer = []
        self.steps = {
            RIGHT: [(self.speed,0)]*self.steps_per_tile,
            LEFT: [(-self.speed,0)]*self.steps_per_tile,
            UP: [(0,-self.speed)]*self.steps_per_tile,
            DOWN: [(0,self.speed)]*self.steps_per_tile
        }
        self.current_direction = RIGHT
        self.current_instruction = None
        self.instructions = []
        self.level = level

    def update(self):
        #scatter
        if ()
        target = self.get_target_tile()
        distance_target = math.sqrt((current_tile[0] - target[0])**2 + (current_tile[1] - target[1])**2)


    def draw(self, shake_x, shake_y):
        if pyxel.frame_count % 15 == 0:
            self.current_animation_frame = (self.current_animation_frame + 1) % 2

        pyxel.blt(self.absolute_position[0] + shake_x, self.absolute_position[1] + shake_y, 0, 
            self.animation_frames[self.persona][self.current_direction][self.current_animation_frame][0], 
            self.animation_frames[self.persona][self.current_direction][self.current_animation_frame][1], 
            8, 8, 0)

    def get_target_tile(self):
        return self.home_tiles[self.persona]
    
    def get_direction(self):
        pass

    def get_options(self):
        pass

    def get_next_mode(self, level, mode):
        pass
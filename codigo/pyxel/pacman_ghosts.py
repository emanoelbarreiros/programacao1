import pyxel

BLINKY = 0
PINKY = 1
INKY = 2
CLYDE = 3

RIGHT = 0
LEFT = 1
DOWN = 2
UP = 3

class Ghost:
    def __init__(self, chase_behavior, frightened_behavior, scatter_behavior, speed, game_map, top_offset, tile):
        self.chase_behavior = chase_behavior
        self.frightened_behavior = frightened_behavior
        self.scatter_behavior = scatter_behavior
        self.animation_frames = [
            [[(0,64), (8,64)],[(16,64), (24,64)],[(32,64), (40,64)],[(48,64), (56,64)]], #blinky
            [[(0,48), (8,48)],[(16,48), (24,48)],[(32,48), (40,48)],[(48,48), (56,48)]], #pinly
            [[(0,56), (8,56)],[(16,56), (24,56)],[(32,56), (40,56)],[(48,56), (56,56)]], #inky
            [[(0,72), (8,72)],[(16,72), (24,72)],[(32,72), (40,72)],[(48,72), (56,72)]]  #clyde
        ]
        self.game_map = game_map
        self.speed = speed
        self.steps_per_tile = self.game_map.tile_size // self.speed
        self.tile = tile
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

    def update(self):
        pass

    def draw(self, shake_x, shake_y):
        if pyxel.frame_count % 15 == 0:
            self.current_animation_frame = (self.current_animation_frame + 1) % 2

        pyxel.blt(self.absolute_position[0] + shake_x, self.absolute_position[1] + shake_y, 0, 
            self.animation_frames[BLINKY][self.current_direction][self.current_animation_frame][0], 
            self.animation_frames[BLINKY][self.current_direction][self.current_animation_frame][1], 
            8, 8, 0)
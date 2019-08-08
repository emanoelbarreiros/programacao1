import pyxel
import pygame
import game_map

#character state
STOPPED = 0
WALKING = 1

#character orientation
RIGHT = 0
LEFT = 1
DOWN = 2
UP = 3
AWAY = 4

class Player:
    def __init__(self, game_control, tile, top_offset, game_map):
        self.sound_chomp = pygame.mixer.Sound('pacman_chomp.wav')
        self.game_control = game_control
        self.intended_direction = AWAY
        self.current_direction = self.intended_direction
        self.state = STOPPED
        self.top_offset = top_offset
        self.tile = tile
        self.speed = 1
        self.game_map = game_map
        self.steps_per_tile = int(self.game_map.tile_size // self.speed)
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
        tile = (int((self.absolute_position[1] - self.top_offset) // 8), int(self.absolute_position[0] // 8))
        return tile

    def opposites(self, dir1, dir2):
        return (dir1 == UP and dir2 == DOWN) or (dir1 == DOWN and dir2 == UP) or (dir1 == LEFT and dir2 == RIGHT) or (dir1 == RIGHT and dir2 == LEFT)

    def handle_movement(self):
        move = None
        if self.opposites(self.intended_direction, self.current_direction):
            count = len(self.move_buffer)
            self.move_buffer.clear() #clear the move buffer
            self.move_buffer.extend(self.steps[self.intended_direction][:self.steps_per_tile - count]) #make the character return to the tile base position
            self.current_direction = self.intended_direction

        if len(self.move_buffer) == 0: #will try to move to the next tile
            #calculate tile the character is at, based on absolute position
            tile = self.get_current_tile()
            if self.game_map.is_transport_tile(tile):
                dest_tile = self.game_map.get_transport_destination(tile)
                self.absolute_position = (dest_tile[1]*8, dest_tile[0]*8 + self.top_offset)
                self.move_buffer.extend(self.steps[self.current_direction])
            else:
                intended_tile = None
                steps = None
                line, column = tile
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
            #self.sound_chomp.play(loops=-1)
        #else:
            #self.sound_chomp.stop()

    def handle_food(self):
        tile = self.get_current_tile()
        base_tile_position = (tile[1]*self.game_map.tile_size, tile[0]*self.game_map.tile_size + self.top_offset)
        if self.absolute_position == base_tile_position:
            self.game_map.eat_food(*tile)

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.intended_direction = LEFT
            self.state = WALKING
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.intended_direction = RIGHT
            self.state = WALKING
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.intended_direction = DOWN
            self.state = WALKING
        elif pyxel.btn(pyxel.KEY_UP):
            self.intended_direction = UP
            self.state = WALKING
        
        self.intended_direction = self.intended_direction

        self.handle_movement()
        self.handle_food()

    def draw(self, shake_x, shake_y):
        if self.state == WALKING:
            self.current_animation_frame = (self.current_animation_frame + 1) % 4

        pyxel.blt(self.absolute_position[0] + shake_x, self.absolute_position[1] + shake_y, 0, 
            self.animation_frames[self.current_direction][self.current_animation_frame][0], 
            self.animation_frames[self.current_direction][self.current_animation_frame][1], 
            8, 8, 0)
import pyxel
import pygame
import ghosts
import player
import game_map
import random

class Game:
    def __init__(self):
        pyxel.init(184, 210, fps=30)
        pyxel.load('pacman.pyxel')
        pygame.mixer.init()
        pygame.mixer.Sound('pacman_beginning.wav').play()
        self.top_offset = 20
        #read map data from file
        with open('map1.txt') as f:
            map_data = f.readlines()
        map_data = [l.strip() for l in map_data]
        self.game_map = game_map.GameMap(self, map_data, self.top_offset)
        self.player_tile = (12,11)
        self.player = player.Player(self, self.player_tile, self.top_offset, self.game_map)
        self.blinky = ghosts.Ghost(1, self.game_map, self.top_offset, (8,11), ghosts.BLINKY)
        self.pinky = ghosts.Ghost(1, self.game_map, self.top_offset, (10,11), ghosts.PINKY)
        self.inky = ghosts.Ghost(1, self.game_map, self.top_offset, (10,9), ghosts.INKY)
        self.clyde = ghosts.Ghost(1, self.game_map, self.top_offset, (10,13), ghosts.CLYDE)
        self.shake = 0
        #never put code after this line, it will not be executed
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.update()
    
    def draw(self):
        pyxel.cls(0)
        shake_x = random.randrange(-2, 2) * self.shake
        shake_y = random.randrange(-2, 2) * self.shake

        self.game_map.draw(shake_x, shake_y)
        self.blinky.draw(shake_x, shake_y)
        self.pinky.draw(shake_x, shake_y)
        self.inky.draw(shake_x, shake_y)
        self.clyde.draw(shake_x, shake_y)
        self.player.draw(shake_x, shake_y)
        
        self.shake *= 0.5
        if self.shake <= 0.05:
            self.shake = 0

Game()
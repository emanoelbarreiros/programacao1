import pyxel

class Map:
    def __init__(self):
        self.spec = []

class Player:
    def __init__(self, position, character_type):
        self.position = position

class Ghost:
    def __init__(self, position, personality):
        self.position = position
        self.personality = personality

class Game:
    def __init__(self):
        pyxel.init(255, 255)

        # game initialization logic here

        pyxel.run(self.update, self.draw)

    def update(self):
        pass
    
    def draw(self):
        pass

Game()
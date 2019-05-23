import pyxel
import random

class Gato:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidade = random.randint(1, 10)
    
    def update(self):
        self.y += self.velocidade

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16)

class Jogo:
    def __init__(self):
        self.gatos = []
        pyxel.init(200, 200)
        pyxel.mouse(True)
        pyxel.load('gato.pyxel')
        pyxel.run(self.update, self.draw)

    def update(self):
        for gato in self.gatos:
            gato.update()

        if pyxel.btnp(pyxel.KEY_LEFT_BUTTON):
            gato = Gato(pyxel.mouse_x, pyxel.mouse_y)
            self.gatos.append(gato)
        
    def draw(self):
        pyxel.cls(0)
        for gato in self.gatos:
            gato.draw()

Jogo()
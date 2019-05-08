import pyxel

CIMA = 0
DIREITA = 1
BAIXO = 2
ESQUERDA = 3

class Snake:
    def __init__(self):
        pyxel.init(200, 200)

        self.cobra = [(100,100), (95, 100), (90, 100), (85, 100), (80, 100), (75,100)]
        self.direcao = DIREITA
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.frame_count % 2 == 0:
            #movimenta de acordo com entrada do usuario
            if pyxel.btn(pyxel.KEY_UP) and self.direcao != BAIXO:
                self.direcao = CIMA
            elif pyxel.btn(pyxel.KEY_RIGHT) and self.direcao != ESQUERDA:
                self.direcao = DIREITA
            elif pyxel.btn(pyxel.KEY_DOWN) and self.direcao != CIMA:
                self.direcao = BAIXO
            elif pyxel.btn(pyxel.KEY_LEFT) and self.direcao != DIREITA:
                self.direcao = ESQUERDA

            #atualiza estado da cobra
            cabeca = self.cobra[0]

            if self.direcao == CIMA:
                cabeca = (cabeca[0], cabeca[1] - 5)
            elif self.direcao == DIREITA:
                cabeca = (cabeca[0] + 5, cabeca[1])
            elif self.direcao == BAIXO:
                cabeca = (cabeca[0], cabeca[1] + 5)
            elif self.direcao == ESQUERDA:
                cabeca = (cabeca[0] - 5, cabeca[1])

            self.cobra.insert(0, cabeca)
            self.cobra.pop(-1)

    def draw(self):
        pyxel.cls(0)
        for segmento in self.cobra:
            pyxel.rect(segmento[0], segmento[1], segmento[0] + 5, segmento[1] + 5, 3)

Snake()
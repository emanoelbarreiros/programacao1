import pyxel
import random

#direcoes da cobra
CIMA = 0
DIREITA = 1
BAIXO = 2
ESQUERDA = 3

#modos de jogo
JOGANDO = 0
GAME_OVER = 1

class Snake:
    def __init__(self):
        pyxel.init(208, 208)
        self.tamanho_segmento = 8
        self.cobra = [(104,104), (96, 104), (88, 104)]
        self.direcao = DIREITA
        self.comida = self.nova_comida()
        self.modo_jogo = JOGANDO
        pyxel.load('snake.pyxel')
        pyxel.run(self.update, self.draw)

    def update(self):
        #movimenta de acordo com entrada do usuario
        if pyxel.btn(pyxel.KEY_UP) and self.direcao != BAIXO:
            self.direcao = CIMA
        elif pyxel.btn(pyxel.KEY_RIGHT) and self.direcao != ESQUERDA:
            self.direcao = DIREITA
        elif pyxel.btn(pyxel.KEY_DOWN) and self.direcao != CIMA:
            self.direcao = BAIXO
        elif pyxel.btn(pyxel.KEY_LEFT) and self.direcao != DIREITA:
            self.direcao = ESQUERDA

        if pyxel.frame_count % 2 == 0 and self.modo_jogo == JOGANDO:
            #atualiza estado da cobra
            cabeca = self.cobra[0]

            if self.direcao == CIMA:
                if cabeca[1] - self.tamanho_segmento < 0: #fazer o wrap
                    cabeca = (cabeca[0], pyxel.height - self.tamanho_segmento)
                else:
                    cabeca = (cabeca[0], cabeca[1] - self.tamanho_segmento)
            elif self.direcao == DIREITA:
                if cabeca[0] + self.tamanho_segmento > pyxel.width - self.tamanho_segmento:
                    cabeca = (0, cabeca[1])
                else:
                    cabeca = (cabeca[0] + self.tamanho_segmento, cabeca[1])
            elif self.direcao == BAIXO:
                if cabeca[1] + self.tamanho_segmento > pyxel.height - self.tamanho_segmento:
                    cabeca = (cabeca[0], 0)
                else:
                    cabeca = (cabeca[0], cabeca[1] + self.tamanho_segmento)
            elif self.direcao == ESQUERDA:
                if cabeca[0] - self.tamanho_segmento < 0:
                    cabeca = (pyxel.width - self.tamanho_segmento, cabeca[1])
                else:
                    cabeca = (cabeca[0] - self.tamanho_segmento, cabeca[1])

            if cabeca[0] == self.comida[0] and cabeca[1] == self.comida[1]:
                self.comida = self.nova_comida()
            else:
                self.cobra.pop(-1)

            for segmento in self.cobra:
                if segmento == cabeca:
                    self.modo_jogo = GAME_OVER

            self.cobra.insert(0, cabeca)

    def nova_comida(self):
        comida = (random.randrange(self.tamanho_segmento, pyxel.width - self.tamanho_segmento, self.tamanho_segmento), random.randrange(self.tamanho_segmento, pyxel.height - self.tamanho_segmento, self.tamanho_segmento)) 
        return comida

    def draw(self):
        pyxel.cls(0)
        for segmento in self.cobra:
            pyxel.rect(segmento[0], segmento[1], segmento[0] + self.tamanho_segmento, segmento[1] + self.tamanho_segmento, 3)

        pyxel.blt(self.comida[0], self.comida[1], 0, 0, 0, 8, 8)
        pyxel.text(10, 10, '({},{})'.format(self.cobra[0][0], self.cobra[0][1]), 7)
        pyxel.text(10, 20, '({},{})'.format(self.comida[0], self.comida[1]), 8)
Snake()
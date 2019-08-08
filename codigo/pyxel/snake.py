import pyxel
import random

#direcoes da cobra
CIMA = 0
DIREITA = 1
BAIXO = 2
ESQUERDA = 3
MESMA_LINHA = 4

#modos de jogo
JOGANDO = 0
GAME_OVER = 1

#tipos de maca
NORMAL = 0
EXTRA = 1

class Segmento:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        pyxel.init(208, 208)
        self.tamanho_segmento = 8
        self.cobra = [Segmento(104,104), Segmento(96,104), Segmento(88,104)]
        self.direcao = DIREITA
        self.comida = self.nova_comida(NORMAL)
        self.modo_jogo = JOGANDO
        self.score = 0
        self.pontuacao_padrao = 8
        self.pontuacao_extra = 40
        self.macas_comidas = 0
        self.timer_pontuacao = 0
        self.tipo_rabo = True
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

        if pyxel.frame_count % 5 == 0 and self.modo_jogo == JOGANDO:
            #atualiza estado da cobra
            self.timer_pontuacao += 1
            cabeca = self.cobra[0]

            if self.direcao == CIMA:
                if cabeca.y - self.tamanho_segmento < 0: #fazer o wrap
                    cabeca = Segmento(cabeca.x, pyxel.height - self.tamanho_segmento)
                else:
                    cabeca = Segmento(cabeca.x, cabeca.y - self.tamanho_segmento)
            elif self.direcao == DIREITA:
                if cabeca.x + self.tamanho_segmento > pyxel.width - self.tamanho_segmento:
                    cabeca = Segmento(0, cabeca.y)
                else:
                    cabeca = Segmento(cabeca.x + self.tamanho_segmento, cabeca.y)
            elif self.direcao == BAIXO:
                if cabeca.y + self.tamanho_segmento > pyxel.height - self.tamanho_segmento:
                    cabeca = Segmento(cabeca.x, 0)
                else:
                    cabeca = Segmento(cabeca.x, cabeca.y + self.tamanho_segmento)
            elif self.direcao == ESQUERDA:
                if cabeca.x - self.tamanho_segmento < 0:
                    cabeca = Segmento(pyxel.width - self.tamanho_segmento, cabeca.y)
                else:
                    cabeca = Segmento(cabeca.x - self.tamanho_segmento, cabeca.y)

            if self.comida[2] == EXTRA and self.timer_pontuacao == self.pontuacao_extra:
                self.comida = self.nova_comida(NORMAL)

            if cabeca.x == self.comida[0] and cabeca.y == self.comida[1]:                
                self.macas_comidas += 1

                if self.comida[2] == EXTRA:
                    self.score += self.pontuacao_extra - self.timer_pontuacao
                else:
                    self.score += self.pontuacao_padrao
                
                if self.macas_comidas % 4 == 0:
                    self.comida = self.nova_comida(EXTRA)
                    self.timer_pontuacao = 0
                else:
                    self.comida = self.nova_comida(NORMAL)
            else:
                self.cobra.pop(-1)

            for segmento in self.cobra:
                if segmento == cabeca:
                    self.modo_jogo = GAME_OVER

            self.cobra.insert(0, cabeca)

    def nova_comida(self, tipo):
        comida = (random.randrange(self.tamanho_segmento, pyxel.width - self.tamanho_segmento, self.tamanho_segmento), random.randrange(self.tamanho_segmento, pyxel.height - self.tamanho_segmento, self.tamanho_segmento), tipo)
        return comida

    def draw(self):
        pyxel.cls(0)
        if pyxel.frame_count % 5 == 0:
            self.tipo_rabo = not self.tipo_rabo
        for i, segmento in enumerate(self.cobra):
            if i == 0:
                if self.direcao == ESQUERDA:
                    pyxel.blt(segmento.x, segmento.y, 0, 32, 16, 8, 8, 0)
                elif self.direcao == DIREITA:
                    pyxel.blt(segmento.x, segmento.y, 0, 0, 16, 8, 8, 0)
                elif self.direcao == BAIXO:
                    pyxel.blt(segmento.x, segmento.y, 0, 16, 16, 8, 8, 0)
                elif self.direcao == CIMA:
                    pyxel.blt(segmento.x, segmento.y, 0, 32, 0, 8, 8, 0)
            else:
                if i + 1 < len(self.cobra):
                    #if self.
                    pyxel.rect(segmento.x, segmento.y, segmento.x + self.tamanho_segmento, segmento.y + self.tamanho_segmento, 3)
                else: # pintar rabinho
                    if self.tipo_rabo:
                        pyxel.blt(segmento.x, segmento.y, 0, 0, 32, 8, 8, 0)
                    else:
                        pyxel.blt(segmento.x, segmento.y, 0, 8, 32, 8, 8, 0)


        pyxel.blt(self.comida[0], self.comida[1], 0, 0, 0, 8, 8)
        pyxel.text(10, 10, 'SCORE {}'.format(self.score), 7)

Snake()
import pyxel
import geometria as g
from geometria import Ponto

ATIVO = 0
PARADO = 1

class Bola:
    def __init__(self, raio, pos, vel_x, vel_y):
        self.raio = raio
        self.pos = pos
        self.vel_x = vel_x
        self.vel_y = vel_y

    def atualizar_pos(self):
        x = self.pos.x + self.vel_x
        y = self.pos.y + self.vel_y 
        self.pos = Ponto(x, y)

class Breakout2:
    def __init__(self):
        pyxel.init(200,200)
        pyxel.load('breakout2.pyxel')
        self.vidas = 3
        self.coracoes = [True] * self.vidas
        self.raio = 3
        self.modo = PARADO
        self.debug = False
        self.pad_l = 50
        self.pad_a = 6
        self.pad_offset = 7
        self.p_sup_esq = None
        self.p_inf_esq = None
        self.p_sup_dir = None
        self.p_inf_dir = None
        self.pad_vel = 0
        self.pos_anterior_bola = None
        self.resetar_posicoes()
        pyxel.run(self.atualizar, self.desenhar)

    def resetar_posicoes(self):
        self.pad_pos = Ponto(pyxel.width/2 - self.pad_l/2, pyxel.height - self.pad_offset - self.pad_a)
        pos = Ponto(pyxel.width/2, self.pad_pos.y - self.raio - 1)
        self.bola = Bola(self.raio, pos, 0, 0)
        self.pos_anterior_bola = pos
        self.atualizar_bounding_box()

    def atualizar_bounding_box(self):
        self.p_sup_esq = Ponto(self.pad_pos.x - self.bola.raio, self.pad_pos.y - self.bola.raio)
        self.p_inf_esq = Ponto(self.p_sup_esq.x, self.p_sup_esq.y + 2*self.bola.raio + self.pad_a)
        self.p_sup_dir = Ponto(self.p_sup_esq.x + 2*self.bola.raio + self.pad_l, self.p_sup_esq.y)
        self.p_inf_dir = Ponto(self.p_sup_dir.x, self.p_sup_dir.y + 2*self.bola.raio + self.pad_a)

    def atualizar(self):
        self.pos_anterior_bola = self.bola.pos

        if self.bola.pos.x <= self.bola.raio or self.bola.pos.x >= pyxel.width - self.bola.raio:
            self.bola.vel_x = -self.bola.vel_x

        if self.bola.pos.y <= self.bola.raio:
            self.bola.vel_y = -self.bola.vel_y

        if self.bola.pos.y >= pyxel.height - self.bola.raio:
            self.vidas -= 1
            self.coracoes[self.vidas] = False
            self.modo = PARADO
            self.resetar_posicoes()

        if pyxel.btn(pyxel.KEY_LEFT):
            self.pad_vel = -8 
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.pad_vel = 8
        elif self.modo == PARADO and pyxel.btn(pyxel.KEY_SPACE):
            self.bola.vel_y = -3
            if self.pad_pos.x + self.pad_l/2 > pyxel.width/2:
                self.bola.vel_x = -3
            else:
                self.bola.vel_x = 3
            self.modo = ATIVO
        else:
            self.pad_vel = self.pad_vel / 1.5

        self.pad_pos.x += self.pad_vel
        self.atualizar_bounding_box()

        if self.modo == ATIVO:
            self.bola.atualizar_pos()
        else:
            pos = Ponto(self.pad_pos.x + self.pad_l/2, self.pad_pos.y - self.raio - 1)
            self.bola.pos = pos

        #checa colisao com a face superior da plataforma
        ponto = g.interseccao(self.pos_anterior_bola, self.bola.pos,
                    self.p_sup_esq, self.p_sup_dir)
        if ponto:
            self.bola.pos = Ponto(ponto.x, ponto.y - 1)
            self.bola.vel_y = -self.bola.vel_y

        #checa colisao com a face esquerda
        ponto = g.interseccao(self.pos_anterior_bola, self.bola.pos,
                    self.p_sup_esq, self.p_inf_esq)
        if ponto:
            self.bola.pos = Ponto(ponto.x - 1, ponto.y)
            self.bola.vel_x = -self.bola.vel_x

        #checa colisao com a face direita
        ponto = g.interseccao(self.pos_anterior_bola, self.bola.pos,
                    self.p_sup_dir, self.p_inf_dir)
        if ponto:
            self.bola.pos = Ponto(ponto.x + 1, ponto.y)
            self.bola.vel_x = -self.bola.vel_x

    def desenhar(self):
        pyxel.cls(1)
        pyxel.circ(self.bola.pos.x, self.bola.pos.y, self.bola.raio, 10)
        pyxel.rect(self.pad_pos.x, self.pad_pos.y, 
            self.pad_pos.x+self.pad_l, self.pad_pos.y + self.pad_a, 3)
        if self.debug:
            pyxel.rectb(self.p_sup_esq.x, self.p_sup_esq.y, self.p_inf_dir.x, self.p_inf_dir.y, 8)
        
        offset_coracoes = (3, 2)
        for i, c in enumerate(self.coracoes):
            x = i*10 + offset_coracoes[0]
            y = offset_coracoes[1]       
            if c:
                pyxel.blt(x, y, 0, 0, 0, 8, 8, 0)
            else:
                pyxel.blt(x, y, 0, 8, 0, 8, 8, 0)

Breakout2()

import pyxel

ATIVO = 0
PARADO = 1

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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
        self.raio = 5
        self.modo = PARADO
        self.debug = False
        self.pad_l = 50
        self.pad_a = 6
        self.pad_offset = 7
        self.pad_pos = Ponto(pyxel.width/2 - self.pad_l/2, pyxel.height - self.pad_offset - self.pad_a)
        pos = Ponto(pyxel.width/2, self.pad_pos.y - self.raio - 2)
        self.bola = Bola(self.raio, pos, 2, 3)
        self.p_sup_esq = None
        self.p_inf_esq = None
        self.p_sup_dir = None
        self.p_inf_dir = None
        self.atualizar_bounding_box()
        self.pad_vel = 0
        self.pos_anterior_bola = None
        self.p1 = Ponto(10, 10)
        self.p2 = Ponto(90, 100)
        self.p3 = self.p1
        self.p4 = self.p2

        pyxel.run(self.atualizar, self.desenhar)

    def atualizar_bounding_box(self):
        self.p_sup_esq = Ponto(self.pad_pos.x - self.bola.raio, self.pad_pos.y - self.bola.raio)
        self.p_inf_esq = Ponto(self.p_sup_esq.x, self.p_sup_esq.y + 2*self.bola.raio + self.pad_a)
        self.p_sup_dir = Ponto(self.p_sup_esq.x + 2*self.bola.raio + self.pad_l, self.p_sup_esq.y)
        self.p_inf_dir = Ponto(self.p_sup_dir.x, self.p_sup_dir.y + 2*self.bola.raio + self.pad_a)

    def interseccao(self, p1, p2, p3, p4):
        """ 
        Implementacao baseada em http://www.dpi.inpe.br/gilberto/livro/bdados/cap2.pdf
        """
        den = (p4.y - p3.y)*(p2.x - p1.x) - (p4.x - p3.x)*(p2.y - p1.y)

        num1 = (p4.x - p3.x)*(p1.y - p3.y) - (p4.y - p3.y)*(p1.x - p3.x)
        num2 = (p2.x - p1.x)*(p1.y - p3.y) - (p2.y - p1.y)*(p1.x - p3.x)
        #nao ha interseccao
        #den == 0 -> segmentos paralelos
        #num1 == 0 e num2 == 0 -> segmentos colineares
        if den == 0 or (num1 == 0 and num2 == 0):
            return None

        u = num1/den
        v = num2/den

        if u >= 0 and u <= 1 and v >= 0 and v <= 1:
            #calcula ponto de intersecao
            x_intersec = p1.x + u*(p2.x - p1.x)
            y_intersec = p1.y + u*(p2.y - p1.y)
            return Ponto(x_intersec, y_intersec)
        else:
            #ha interseccao, mas fora dos segmentos
            return None

    def atualizar(self):
        self.pos_anterior_bola = self.bola.pos

        if self.bola.pos.x <= self.bola.raio or self.bola.pos.x >= pyxel.width - self.bola.raio:
            self.bola.vel_x = -self.bola.vel_x

        if self.bola.pos.y <= self.bola.raio or self.bola.pos.y >= pyxel.height - self.bola.raio:
            self.bola.vel_y = -self.bola.vel_y

        if pyxel.btn(pyxel.KEY_LEFT):
            self.pad_vel = -8 
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.pad_vel = 8
        elif self.modo == PARADO and pyxel.btn(pyxel.KEY_SPACE):
            print('espaco')
            #self.bola.pos.y -= 2
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
            pos = Ponto(self.pad_pos.x + self.pad_l/2, self.pad_pos.y - self.raio)
            self.bola.pos = pos
        
        self.p3 = Ponto(pyxel.mouse_x, pyxel.mouse_y)
        self.p4 = Ponto(self.p3.x + 80, self.p3.y)

        #checa colisao com a face superior da plataforma
        ponto = self.interseccao(self.pos_anterior_bola, self.bola.pos,
                    self.p_sup_esq, self.p_sup_dir)
        if ponto:
            self.bola.pos = Ponto(ponto.x, ponto.y - 1)
            self.bola.vel_y = -self.bola.vel_y

        #checa colisao com a face esquerda
        ponto = self.interseccao(self.pos_anterior_bola, self.bola.pos,
                    self.p_sup_esq, self.p_inf_esq)
        if ponto:
            self.bola.pos = Ponto(ponto.x - 1, ponto.y)
            self.bola.vel_x = -self.bola.vel_x

        #checa colisao com a face direita
        ponto = self.interseccao(self.pos_anterior_bola, self.bola.pos,
                    self.p_sup_dir, self.p_inf_dir)
        if ponto:
            self.bola.pos = Ponto(ponto.x + 1, ponto.y)
            self.bola.vel_x = -self.bola.vel_x

    def desenhar(self):
        pyxel.cls(1)
        pyxel.circ(self.bola.pos.x, self.bola.pos.y, self.bola.raio, 10)
        pyxel.rect(self.pad_pos.x, self.pad_pos.y, 
            self.pad_pos.x+self.pad_l, self.pad_pos.y + self.pad_a, 3)
        # pyxel.line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, 7)
        # pyxel.line(self.p3.x, self.p3.y, self.p4.x, self.p4.y, 7)
        # ponto = self.interseccao(self.p1, self.p2, self.p3, self.p4)
        # if ponto:
        #     pyxel.circ(ponto.x, ponto.y, 2, 8)
        if self.debug:
            pyxel.rectb(self.p_sup_esq.x, self.p_sup_esq.y, self.p_inf_dir.x, self.p_inf_dir.y, 8)


Breakout2()

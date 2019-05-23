import pyxel

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, outro):
        return Ponto(self.x + outro.x, self.y + outro.y)

class Breakout:
    def __init__(self):
        pyxel.init(255, 255, caption="Duel")
        self.pos_atual_bola = Ponto(pyxel.width/2, pyxel.height/2)
        self.pos_anterior_bola = Ponto(pyxel.width/2, pyxel.height/2)
        self.vel_x = 4
        self.vel_y = 3
        self.raio_bola = 4
        self.pos_caixa = Ponto(0, 0)
        self.caixa_l = 50
        self.caixa_a = 50
        self.ponto_intersec = None
        self.p1 = Ponto(30, 30)
        self.p2 = Ponto(100, 100)

        pyxel.run(self.update, self.draw)

    def interseccao(self, p1, p2, p3, p4):
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

    def update(self):
        self.pos_anterior_bola = self.pos_atual_bola
        x = self.pos_atual_bola.x
        y = self.pos_atual_bola.y
        self.pos_atual_bola = Ponto(x + self.vel_x, y + self.vel_y)
        
        if self.pos_atual_bola.x > pyxel.width - self.raio_bola or self.pos_atual_bola.x < 0: 
            self.vel_x = -self.vel_x
        if self.pos_atual_bola.y > pyxel.height - self.raio_bola or self.pos_atual_bola.y < 0:
            self.vel_y = -self.vel_y

        #testa interseccao com o segumento superior da caixa
        ponto_sup_dir = Ponto(self.pos_caixa.x + self.caixa_l, self.pos_caixa.y)
        ponto = self.interseccao(self.pos_anterior_bola, self.pos_atual_bola, self.pos_caixa, ponto_sup_dir)
        if ponto:
            self.pos_atual_bola = ponto + Ponto(0,-1)
            self.vel_y = -self.vel_y

        #testa interseccao com o segumento direito da caixa
        ponto_inf_dir = Ponto(ponto_sup_dir.x, ponto_sup_dir.y + self.caixa_a)
        ponto = self.interseccao(self.pos_anterior_bola, self.pos_atual_bola, ponto_sup_dir, ponto_inf_dir)
        if ponto:
            self.pos_atual_bola = ponto + Ponto(1,0)
            self.vel_x = -self.vel_x

        #testa interseccao com o segumento esquerdo da caixa
        ponto_inf_esq = self.pos_caixa + Ponto(0, self.caixa_a)
        ponto = self.interseccao(self.pos_anterior_bola, self.pos_atual_bola, self.pos_caixa, ponto_inf_esq)
        if ponto:
            self.pos_atual_bola = ponto + Ponto(-1,0)
            self.vel_x = -self.vel_x

        self.pos_caixa.x = pyxel.mouse_x
        self.pos_caixa.y = pyxel.mouse_y

    def draw(self):
        pyxel.cls(1)
        pyxel.circ(self.pos_atual_bola.x, self.pos_atual_bola.y, self.raio_bola, 7)
        pyxel.rectb(self.pos_caixa.x, self.pos_caixa.y, self.pos_caixa.x+self.caixa_l, self.pos_caixa.y+self.caixa_a, 10)
        pyxel.line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, 7)
        ponto = self.interseccao(self.p1, self.p2, self.pos_caixa, self.pos_caixa+Ponto(self.caixa_l,0))
        if ponto:
            pyxel.circ(ponto.x, ponto.y, 3, 8)



Breakout()
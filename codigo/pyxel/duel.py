import pyxel
import random
import math

#modos do inimigo
INVISIVEL = 0
EM_MOVIMENTO = 1
ATIROU = 2
MORRENDO = 3
MORTO = 4

#modos de jogo
INICIO = 0
ATIRANDO = 1
INIMIGO_MORTO = 2
GAME_OVER = 3

raio_tiro = 3 #pixels
espera_apos_acerto = 30 #frames

class Vetor:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Inimigo:
    def __init__(self, frames_por_passo, larg_mundo, alt_mundo, app, posicao=None):
        self.ticks = 0
        self.frames_por_passo = frames_por_passo
        self.passo_animacao = 0
        self.sprite_em_branco = (32, 112)
        self.sprite_vivo = (0, 0)
        self.sprite_atirou = (48, 0)
        self.sprite_morto = (48, 16)
        self.sprite = self.sprite_vivo
        self.raio_sprite = 6 #pixels
        self.larg_mundo = larg_mundo
        self.alt_mundo = alt_mundo
        self.app = app
        
        if posicao:
            self.posicao = posicao
        else:
            x_inimigo = random.randint(20, self.larg_mundo - 20)
            y_inimigo = random.randint(20, self.alt_mundo - 20)
            self.posicao = Vetor(x_inimigo, y_inimigo)

        self.estado = INVISIVEL
            
        #self.animacao_tiro = [(0,0), (16,0), (32,0), (48,0)]
        #self.animacao_morto = [(0,16), (16,16), (32,16), (48,16)]

    def resetar(self):
        self.estado = INVISIVEL

        x_inimigo = random.randint(20, self.larg_mundo - 20)
        y_inimigo = random.randint(20, self.alt_mundo - 20)
        self.posicao = Vetor(x_inimigo, y_inimigo)

        self.estado = EM_MOVIMENTO

    def atualizar(self):
        self.ticks += 1
        if self.ticks >= self.frames_por_passo:
            if self.estado == EM_MOVIMENTO:
                self.estado = ATIROU
                self.app.notificar_tiro()
            if self.estado == MORRENDO:
                self.estado = MORTO

            self.ticks = 0

    def ativar(self):
        self.estado = EM_MOVIMENTO
        self.ticks = 0

    def matar(self):
        self.estado = MORTO

    def desenhar(self):
        if self.estado == EM_MOVIMENTO:
            #fazer animacao de movimento depois, inicialmente só colocar o sprite dele morto
            sprite = self.sprite_vivo    
        elif self.estado == ATIROU:
            sprite = self.sprite_atirou
        elif self.estado == MORTO:
            sprite = self.sprite_morto
        else:
            sprite = self.sprite_em_branco

        pyxel.blt(self.posicao.x-8, self.posicao.y-8, 0, sprite[0], sprite[1], 16, 16)

    def acertou(self, x_tiro, y_tiro, raio_tiro):
        return self.distancia_int(self.posicao.x, self.posicao.y, x_tiro, y_tiro) <= self.raio_sprite + raio_tiro

    def distancia_int(self, x1, y1, x2, y2):
        return int(math.sqrt((x1-x2)**2 + (y1-y2)**2))


class Jogo:
    def __init__(self):
        pyxel.init(255, 255, caption="Duel")
        self.score = 0
        self.modo_jogo = INICIO
        self.contador_frames_acerto = 0
        #deixar o mouse invisivel
        pyxel.mouse(False)
        #carregar arquivo de assets
        pyxel.load('duel.pyxel')
        self.tiros = []

        self.inimigo = Inimigo(60, pyxel.width, pyxel.height, self)
        
        #essa tem que ser a ultima linha do metodo __init__, tudo apos isso sera ignorado
        pyxel.run(self.update, self.draw)

    def notificar_tiro(self):
        self.modo_jogo = GAME_OVER

    def update(self):
        self.inimigo.atualizar()

        if pyxel.btn(pyxel.KEY_S):
            self.tiros = []
            self.inimigo.ativar()
            self.modo_jogo = ATIRANDO

        if self.modo_jogo == ATIRANDO:
            #detecta se houve tiro
            if pyxel.btnp(pyxel.KEY_LEFT_BUTTON):
                self.tiros.append(Vetor(pyxel.mouse_x, pyxel.mouse_y))
                if self.inimigo.acertou(pyxel.mouse_x, pyxel.mouse_y, raio_tiro):
                    self.inimigo.matar()
                    self.modo_jogo = INIMIGO_MORTO
                    self.score += 1
        elif self.modo_jogo == INIMIGO_MORTO:       
            self.contador_frames_acerto += 1
            if self.contador_frames_acerto > espera_apos_acerto:
                self.tiros = []
                self.modo_jogo = ATIRANDO
                self.inimigo = self.inimigo = Inimigo(30, pyxel.width, pyxel.height, self)
                self.inimigo.ativar()
                self.contador_frames_acerto = 0
        elif self.modo_jogo == GAME_OVER:
            if pyxel.btn(pyxel.KEY_R):
                self.tiros = []
                self.inimigo = Inimigo(30, pyxel.width, pyxel.height, self)
                self.modo_jogo = INICIO
                self.score = 0

    def draw(self):
        pyxel.cls(7)
        self.inimigo.desenhar()
        #desenhar tiros
        for tiro in self.tiros:
            pyxel.blt(tiro.x - 8, tiro.y - 8, 0, 0, 112, 16, 16, 7)
        #desenha score
        pyxel.text(10, 10, 'SCORE {}'.format(self.score), 1)
        #desenha mira
        pyxel.blt(pyxel.mouse_x - 8, pyxel.mouse_y - 8, 0, 16, 112, 16, 16, 7)

        
Jogo()
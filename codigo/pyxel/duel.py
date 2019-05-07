import pyxel
import random
import math

#modos do inimigo
INVISIVEL = 0
VIVO = 1
ATIROU = 2
MORRENDO = 3
MORTO = 4

#modos de jogo
INICIO = 0
ATIRANDO = 1
INIMIGO_MORTO = 2
GAME_OVER = 3

raio_tiro = 3 #pixels

class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Inimigo:
    duracao_frame_vivo = 10
    duracao_frame_morte = 7
    sprite_em_branco = (32, 112)
    sprite_vivo = (0, 0)
    sprite_atirou = (48, 0)
    sprite_morto = (64,16)
    animacao_vivo = [(0,0), (16,0), (32,0), (48,0)]
    animacao_morte = [(0,16), (16, 16), (32,16), (48,16), (64,16)]

    def __init__(self, larg_mundo, alt_mundo, app, posicao=None):
        self.ticks = 0
        self.ticks_animacao = 0
        self.frame_atual_animacao_vivo = -1
        self.frame_atual_animacao_morte = -1
        self.passo_animacao = 0
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

        self.estado = VIVO

    def atualizar(self):
        self.ticks += 1
        #gerenciar estados do inimigo
        if self.estado == VIVO and self.frame_atual_animacao_vivo == len(self.animacao_vivo) - 1:
            self.estado = ATIROU
            self.app.notificar_tiro()
                
        if self.estado == MORRENDO and self.frame_atual_animacao_morte == len(self.animacao_morte) - 1:
            self.estado = MORTO

    def ativar(self):
        self.estado = VIVO
        self.frame_atual_animacao_vivo = 0
        self.frame_atual_animacao_morte = 0
        self.ticks_animacao = 0
        self.ticks = 0

    def matar(self):
        self.estado = MORRENDO
        self.ticks_animacao = 0

    def desenhar(self):
        self.ticks_animacao += 1
        if self.estado == VIVO:
            #fazer animacao de movimento depois, inicialmente só colocar o sprite dele morto
            #redutor  = self.ticks//(self.duracao_animacao_vivo//len(animacao_vivo))
            #sprite = animacao_vivo[redutor % len(animacao_vivo)]
            if self.ticks_animacao >= self.duracao_frame_vivo:
                self.ticks_animacao = 0
                self.frame_atual_animacao_vivo += 1
            sprite = self.animacao_vivo[self.frame_atual_animacao_vivo]
        elif self.estado == ATIROU:
            sprite = self.sprite_atirou
        elif self.estado == MORTO:
            sprite = self.sprite_morto
        elif self.estado == MORRENDO:
            #redutor  = self.ticks//(self.duracao_animacao_morte//len(animacao_morte))
            #sprite = animacao_morte[redutor % len(animacao_morte)]    
            if self.ticks_animacao > self.duracao_frame_morte:
                self.ticks_animacao = 0
                self.frame_atual_animacao_morte += 1
            sprite = self.animacao_morte[self.frame_atual_animacao_morte]
        else:
            sprite = self.sprite_em_branco

        pyxel.blt(self.posicao.x - 8, self.posicao.y - 8, 0, sprite[0], sprite[1], 16, 16)

    def acertou(self, x_tiro, y_tiro, raio_tiro):
        return self.distancia_int(self.posicao.x, self.posicao.y, x_tiro, y_tiro) <= self.raio_sprite + raio_tiro

    def distancia_int(self, x1, y1, x2, y2):
        return int(math.sqrt((x1-x2)**2 + (y1-y2)**2))

    @classmethod
    def duracao_morte(cls):
        """Duracao da morte em frames"""
        return len(cls.animacao_morte) * cls.duracao_frame_morte


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

        self.inimigos = []

        self.espera_apos_morto = Inimigo.duracao_morte() + 15
        
        #essa tem que ser a ultima linha do metodo __init__, tudo apos isso sera ignorado
        pyxel.run(self.update, self.draw)

    def notificar_tiro(self):
        self.modo_jogo = GAME_OVER

    def update(self):
        for inimigo in self.inimigos:
            inimigo.atualizar()

        if self.modo_jogo == INICIO and pyxel.btn(pyxel.KEY_S):
            self.tiros = []
            inimigo = Inimigo(pyxel.width, pyxel.height, self)
            self.inimigos.append(inimigo)
            inimigo.ativar()
            self.modo_jogo = ATIRANDO

        if self.modo_jogo == ATIRANDO:
            #detecta se houve tiro
            acertou_tiro = False
            if pyxel.btnp(pyxel.KEY_LEFT_BUTTON):
                pyxel.play(0, 0)
                for inimigo in self.inimigos:
                    if inimigo.acertou(pyxel.mouse_x, pyxel.mouse_y, raio_tiro):
                        inimigo.matar()
                        self.modo_jogo = INIMIGO_MORTO
                        self.score += 1
                        acertou_tiro = True
                if not acertou_tiro:
                    self.tiros.append(Vetor(pyxel.mouse_x, pyxel.mouse_y))
                        
        elif self.modo_jogo == INIMIGO_MORTO:       
            self.contador_frames_acerto += 1
            if self.contador_frames_acerto > self.espera_apos_morto:
                self.tiros = []
                self.modo_jogo = ATIRANDO
                inimigo = Inimigo(pyxel.width, pyxel.height, self)
                self.inimigos.append(inimigo)
                inimigo.ativar()
                self.contador_frames_acerto = 0
        elif self.modo_jogo == GAME_OVER and pyxel.btn(pyxel.KEY_R):
            self.tiros = []
            self.inimigos = []
            self.modo_jogo = INICIO
            self.score = 0  

    def draw(self):
        pyxel.cls(7)
        for inimigo in self.inimigos:
            inimigo.desenhar()
        #desenhar tiros
        for tiro in self.tiros:
            pyxel.blt(tiro.x - 8, tiro.y - 8, 0, 0, 112, 16, 16, 7)
        #desenha score
        pyxel.text(10, 10, 'SCORE {}'.format(self.score), 1)
        #desenha mira
        pyxel.blt(pyxel.mouse_x - 8, pyxel.mouse_y - 8, 0, 16, 112, 16, 16, 7)

        
Jogo()
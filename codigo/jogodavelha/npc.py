from functools import partial
import itertools
import regras

def obter_resultados_possiveis(tabuleiro, possibilidades):
    resultados_possiveis = []
    for possibilidade in possibilidades:
        if eh_subset(tabuleiro, possibilidade):
            resultados_possiveis.append(possibilidade[:])

    return resultados_possiveis

def obter_probabilidades(tabuleiro, possibilidades):
    probabilidades = []
    jogadas = jogadas_possiveis(tabuleiro)
    resultados_possiveis = obter_resultados_possiveis(tabuleiro, possibilidades)
    quantidade_possibilidades = len(resultados_possiveis)
    for jogada in jogadas:
        for possibilidade in resultados_possiveis:
            chance = contabilizar_chance_vitoria(tabuleiro, jogada)
            probabilidades.append( (chance / quantidade_possibilidades, jogada) )

    #ordenar pela chance, primeiro elemento da tupla
    probabilidades.sort(key=lambda tupla: tupla[0])
    return probabilidades

def jogadas_possiveis(tabuleiro):
    jogadas = []
    for l, v_l in enumerate(tabuleiro):
        for c, v_c in enumerate(v_l):
            if v_c == '_':
                jogadas.append((l,c))
    
    return jogadas

def contabilizar_chance_vitoria(tabuleiro, jogada):
    resultado = 0
    jogada_aplicada = aplicar(jogada, tabuleiro)
    if eh_subset(jogada_aplicada, tabuleiro) and regras.ganhador(tabuleiro) == 'O':
        resultado += 1
    
    return resultado

def eh_subset(jogada_aplicada, tabuleiro):
    tabuleiro_parcial_linear = itertools.chain(*jogada_aplicada)
    tabuleiro_linear = itertools.chain(*tabuleiro)

    quantidade_vitorias = 0
    if tabuleiro == None or len(tabuleiro) == 0:
        return True

    for elemento_jogada, elemento_tabuleiro in zip(tabuleiro_parcial_linear, tabuleiro_linear):
        if elemento_jogada != '_' and elemento_jogada != elemento_tabuleiro:
            return False

    return True

def aplicar(jogada, tabuleiro, jogador='O'):
    copia = tabuleiro[:]
    copia[jogada[0]][jogada[1]] = jogador;
    return copia
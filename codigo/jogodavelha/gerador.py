def jogos_possiveis():
    jogos_completos = []
    if len(jogos_completos) == 0:
        tabuleiro_vazio = ['_', '_', '_','_', '_', '_','_', '_', '_']
        tabuleiros_a_preencher = []
        tabuleiros_a_preencher.append({ 'X' : tabuleiro_vazio })
        while len(tabuleiros_a_preencher) > 0:
            #obter a chave do unico registro, jogador a dar a proxima jogada neste tabuleiro
            jogada_tabuleiro = tabuleiros_a_preencher.pop(0)
            jogador_atual = list(jogada_tabuleiro)[0]
            tabuleiro_atual = jogada_tabuleiro[jogador_atual]
            if tabuleiro_atual.count('_') > 0: # ainda existe posicao vazia para ser jogada
                for posicao, valor in enumerate(tabuleiro_atual):
                    if (valor == '_'):
                        tabuleiro_jogado = tabuleiro_atual[:]
                        tabuleiro_jogado[posicao] = jogador_atual
                        tabuleiros_a_preencher.append({ outro_jogador(jogador_atual) : tabuleiro_jogado })
            else: # tabuleiro completo, adicionar a lista final de jogos completos
                jogos_completos.append(tabuleiro_atual)
                
    return jogos_completos

def outro_jogador(jogador):
    if jogador == 'X':
        return 'O'
    else:
        return 'X'
        
def carregar_jogos():
    arquivo = open('jogos.txt')
    entradas = []
    for linha in arquivo.readlines():
        jogo = []
        for car in linha.strip():
            jogo.append(car)
        entradas.append(jogo)

    return entradas

if __name__ == '__main__':
    jogos_completos = jogos_possiveis()
    arquivo = open('jogos.txt', 'w+')
    for jogo in jogos_completos:
        for posicao in jogo:
            arquivo.write(str(posicao))
        arquivo.write('\n')

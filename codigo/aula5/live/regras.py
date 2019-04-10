def jogada_valida(tabuleiro, linha, coluna):
    if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
        return False
    
    if tabuleiro[linha][coluna] != '_':
        return False

    return True

def ganhador(tabuleiro, char_vazio='_'):
    for linha in tabuleiro:
        if iguais(*linha) and linha[0] != char_vazio:
            return linha[0]

    colunas = [col for col in zip(*tabuleiro)]
    for coluna in colunas:
        if iguais(*coluna) and coluna[0] != char_vazio:
            return coluna[0]

    if iguais(tabuleiro[0][0], tabuleiro[1][1], tabuleiro[2][2]) and tabuleiro[0][0] != char_vazio:
        return tabuleiro[0][0]
    
    if iguais(tabuleiro[0][2], tabuleiro[1][1], tabuleiro[2][0]) and tabuleiro[0][2] != char_vazio:
        return tabuleiro[0][2]

    lista_completa = tabuleiro[0] + tabuleiro[1] + tabuleiro[2]
    if lista_completa.count('_') == 0:
        return 'E'
    else:
        return 'N'

def iguais(*valores):
    return valores.count(valores[0]) == len(valores)

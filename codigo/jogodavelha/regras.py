def jogada_valida(tabuleiro, linha, coluna):
    valida = True

    if intervalo_permitido(linha, coluna):
        valida = valida and tabuleiro[linha][coluna] == '_'
    else: 
        valida = False

    return valida

def intervalo_permitido(linha, coluna):
    return linha >= 0 and linha <= 2 and coluna >= 0 and coluna <= 2

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

    lista_total = tabuleiro[0] + tabuleiro[1] + tabuleiro[2]
    if lista_total.count(char_vazio) == 0:
        return 'E' # empate

    return 'N' # nenhum ganhador

def iguais(*valores):
    return valores.count(valores[0]) == len(valores)
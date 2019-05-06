#auxiliar.py

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(*linha, sep=' | ')
            
def soma(tupla1, tupla2):
    return (tupla1[0]+tupla2[0], tupla1[1]+tupla2[1])
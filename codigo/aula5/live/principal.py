import auxiliar
import regras
import os

tabuleiro = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]

print('Bem vindo ao jogo da velha')
print('Para jogar, informe linha e coluna, separados por espaço e pressione Enter.')
print('Exemplo jogando na linha 1, coluna 2: 1 2')
print('O jogador X joga primeiro.')

vez_do_x = True
ganhador = 'N'
while ganhador == 'N':
    os.system('clear')
    if vez_do_x:
        mensagem = 'Vez do X. Informe linha e coluna: '
        jogada_da_vez = 'X'
    else:
        mensagem = 'Vez do O. Informe linha e coluna: '
        jogada_da_vez = 'O'

    jogada = input(mensagem).split()
    linha = int(jogada[0]) - 1
    coluna = int(jogada[1]) - 1

    if regras.jogada_valida(tabuleiro, linha, coluna):
        tabuleiro[linha][coluna] = jogada_da_vez
        auxiliar.imprimir_tabuleiro(tabuleiro)
        vez_do_x = not vez_do_x
        ganhador = regras.ganhador(tabuleiro)
    else:
        print('Jogada inválida, tente novamente.')

if ganhador == 'X':
    print('O X venceu!')
elif ganhador == 'O':
    print('O O venceu!')
else:
    print('Empate, que triste.')
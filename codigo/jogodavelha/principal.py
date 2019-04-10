import auxiliar
import regras

print('Bem vindo ao jogo da velha')
print('Informe linha e coluna para jogar. Linhas e colunas podem ser 1, 2 ou 3.')
print('Informe-as separando com um espaço. Jogar na linha 1, coluna 2 seria: 1 2')
print('Se desejar sair, basta informar Q no lugar de sua jogada.')
print('Boa sorte, o jogador X começa jogando!')
print()

jogadas = 0
jogando = True
tabuleiro = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]

while regras.ganhador(tabuleiro) == 'N':
    if jogadas % 2 == 0:
        mensagem = 'Vez do X. Informe linha e coluna: '
        jogada_pretendida = 'X'
    else:
        mensagem = 'Vez do O. Informe linha e coluna: '
        jogada_pretendida = 'O'
        
    jogada = input(mensagem).split(' ')
    if len(jogada) == 2:
        linha = int(jogada[0]) - 1
        coluna = int(jogada[1]) - 1
    elif len(jogada) == 1 and (jogada[1] == 'q' or jogada[1] == 'Q'):
        print('Obrigado por jogar. Até mais')
    else: 
        print('Informe apenas linha e coluna.')

    if (regras.jogada_valida(tabuleiro, linha, coluna)):
        tabuleiro[linha][coluna] = jogada_pretendida
        auxiliar.imprimir_tabuleiro(tabuleiro)
        jogadas += 1
    else:
        print('Jogada inválida')

ganhador = regras.ganhador(tabuleiro)
print(ganhador)
if ganhador == 'X':
    print('O jogador X venceu!')
elif ganhador == 'O':
    print('O jogador O venceu!')
else:
    print('Empate, triste...')
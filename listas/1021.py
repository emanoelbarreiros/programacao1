carteira = {100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0, 
            0.5:0, 0.25:0, 0.1:0, 0.05:0, 0.01:0}

valor = float(input()) + 0.001

for nota, quantidade in carteira.items():
    numero_notas = valor // nota
    carteira[nota] = numero_notas
    valor = valor % nota

print('NOTAS:')
for nota, quantidade in carteira.items():
    if nota == 1:
        print('MOEDAS:')    

    if (nota > 1):
        print('%d nota(s) de R$ %.2f' % (quantidade, nota))
    else:
        print('%d moeda(s) de R$ %.2f' % (quantidade, nota))

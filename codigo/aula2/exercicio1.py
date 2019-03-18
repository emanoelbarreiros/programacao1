quantidade = input('Informe a quantidade de pessoas: ')
quantidade = int(quantidade)
controle = 0
valor_total = 0
while controle < quantidade:
    controle += 1
    idade = input('Informe a idade: ')
    idade = int(idade)

    if idade >= 3 and idade < 12:
        valor_total = valor_total + 10
    elif idade >= 12:
        valor_total += 20

print(f'Valor total {valor_total}.')
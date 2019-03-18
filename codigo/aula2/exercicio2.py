valor_total = 0
while True:
    entrada = input('Informe a idade para calcular o valor ou "sair" para encerrar o programa: ')
    
    if entrada == 'sair':
        break
    else:
        idade = int(entrada)
        if idade >= 3 and idade < 12:
            valor_total += 10
        elif idade >= 12:
            valor_total += 20

print(f'Valor total é R$ {valor_total:.2f}.')
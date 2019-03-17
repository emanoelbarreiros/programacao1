# este programa calcula o IMC do usuario
altura = input('Qual a sua alatura em centímetros? ')
peso = input('Qual o seu peso em quilos? ')

# altura agora está em metros
altura = float(altura)/100
imc = float(peso) / altura**2

print(f'Seu IMC é de {imc:.2f}.')

classificacao = ''
if imc < 18.5:
    classificacao = 'abaixo do peso'
elif imc >= 18.5 and imc < 25:
    classificacao = 'peso normal'
elif imc >= 25 and imc < 30:
    classificacao = 'sobrepeso'
elif imc >= 30 and imc < 35:
    classificacao = 'obesidade grau 1'
elif imc >= 35 and imc < 40:
    classificacao = 'obesidade grau 2'
else:
    classificacao = 'obesidade grau 3'

print(f'Você foi classificado como {classificacao}.')
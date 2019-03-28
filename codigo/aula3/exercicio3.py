numeros = []

for n in range(1, 11):
    numeros.append(n**2)

print(numeros)

#versao com compreensao de listas tal qual o slide
numeros = [v**2 for v in range(1, 11)]
print(numeros)
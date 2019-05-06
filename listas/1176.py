quantidade_valores = int(input())
valores = []
for i in range(quantidade_valores):
    valores.append(int(input()))

fibonacci = [0, 1]
maior_valor = max(valores)
for i in range(maior_valor + 1):
    fib = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(fib)

for i in valores:
    print('Fib({}) = {}'.format(i, fibonacci[i]))
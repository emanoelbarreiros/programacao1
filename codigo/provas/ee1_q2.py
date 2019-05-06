import math

def resolve_equacao(c1, c2, c3=0):
    if c3 != 0:
        delta = c2**2 - 4 * c3 * c1
        raiz1 = (-c2 + math.sqrt(delta))/2*c3
        raiz2 = (-c2 - math.sqrt(delta))/2*c3

        return (raiz1, raiz2)
    else:
        res = -c1/c2

        return res

def teste():
    res1 = resolve_equacao(3, -2)
    print(res1)
    res2 = resolve_equacao(3, 6, 2)
    print(res2)

if __name__ == '__main__':
    teste()

import numpy as np

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def interseccao(p1, p2, p3, p4):
    """ 
    Implementacao baseada em http://www.dpi.inpe.br/gilberto/livro/bdados/cap2.pdf
    """
    den = (p4.y - p3.y)*(p2.x - p1.x) - (p4.x - p3.x)*(p2.y - p1.y)

    num1 = (p4.x - p3.x)*(p1.y - p3.y) - (p4.y - p3.y)*(p1.x - p3.x)
    num2 = (p2.x - p1.x)*(p1.y - p3.y) - (p2.y - p1.y)*(p1.x - p3.x)
    #nao ha interseccao
    #den == 0 -> segmentos paralelos
    #num1 == 0 e num2 == 0 -> segmentos colineares
    if den == 0 or (num1 == 0 and num2 == 0):
        return None

    u = num1/den
    v = num2/den

    if u >= 0 and u <= 1 and v >= 0 and v <= 1:
        #calcula ponto de intersecao
        x_intersec = p1.x + u*(p2.x - p1.x)
        y_intersec = p1.y + u*(p2.y - p1.y)
        return Ponto(x_intersec, y_intersec)
    else:
        #ha interseccao, mas fora dos segmentos
        return None
    
def rotacionar_ponto(p1, p2, p3):
    a = np.array([p1.x, p1.y])
    b = np.array([p2.x, p2.y])
    c = np.array([p3.x, p3.y])

    ba = a - b
    bc = c - b

    coseno = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angulo = np.arccos(coseno)

    print(np.degrees(angulo))
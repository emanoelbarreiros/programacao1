import ee1_q2

def resolve_equacoes(lista_coefs):
    resultados = []
    for coefs in lista_coefs:
        resultado = ee1_q2.resolve_equacao(*coefs)
        resultados.append(resultado)

    return resultados

def resolve_equacao2(lista_coefs):
    resultados = []
    for coefs in lista_coefs:
        if len(coefs) == 2:
            resultado = ee1_q2.resolve_equacao(coefs[0], coefs[1])
            resultados.append(resultado)
        if len(coefs) == 3:
            resultado = ee1_q2.resolve_equacao(coefs[0], coefs[1], coefs[2])
            resultados.append(resultado)
    
    return resultados

l =[ [3, -2], [3, 6, 2], [10, 5] ]
resultados = resolve_equacoes(l)
print(resultados)
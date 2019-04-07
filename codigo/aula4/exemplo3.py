import random

def obterResposta(numero):
    if numero == 1:
        return 'É certeza!'
    elif numero == 2:
        return 'Muito provavelmente sim.'
    elif numero == 3:
        return 'Sim.'
    elif numero == 4:
        return 'Resposta nebulosa, tente novamente...'
    elif numero == 5:
        return 'Pergunte novamente mais tarde.'
    elif numero == 6:
        return 'Concentre-se e tente novamente.'
    elif numero == 7:
        return 'Minha resposta é não.'
    elif numero == 8:
        return 'A perspectiva não é boa.'
    elif numero == 9:
        return 'Muito duvidoso.'

r = random.randint(1, 9)
resultado = obterResposta(r)
print(resultado)
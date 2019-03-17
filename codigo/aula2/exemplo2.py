ativo = True
while ativo:
    texto = input('Digite algo e eu repito pra você: ')

    if texto == 'cansei':
        print('Tudo bem, até mais.')
        ativo = False
    else:
        print(texto)
        print()

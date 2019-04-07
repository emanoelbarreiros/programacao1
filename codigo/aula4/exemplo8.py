def cafeDaManha():
    ovos = 'cafeDaManha local'
    print(ovos) #exibe 'cafeDaManha local'

def bacon():
    ovos = 'bacon local'
    print(ovos) #exibe 'bacon local'
    cafeDaManha()
    print(ovos) #exibe 'bacon local'

ovos = 'global'
bacon()
print(ovos) #exibe 'global'
def obter_nome_formatado(nome, ultimo_nome, sobrenome=''):
    if sobrenome:
        nome_completo = nome + ' ' + sobrenome + ' ' + ultimo_nome
    else:
        nome_completo = nome + ' ' + ultimo_nome
        
    return nome_completo.title()

nome1 = obter_nome_formatado('emanoel', 'barreiros')
print(nome1)

nome2 = obter_nome_formatado('emanoel', 'barreiros', 'francisco')
print(nome2)

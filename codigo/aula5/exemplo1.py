def obter_nome_formatado(nome, sobrenome, ultimo_nome):
    nome_completo = nome + ' ' + sobrenome + ' ' + ultimo_nome
    return nome_completo.title()

nome = obter_nome_formatado('emanoel', 'francisco', 'barreiros')
print(nome)

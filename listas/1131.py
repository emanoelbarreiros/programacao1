opcao = '1'
vitorias_inter = 0
vitorias_gremio = 0
empates = 0
while opcao == '1':
    gols = input().split()
    gols_inter = int(gols[0])
    gols_gremio = int(gols[1])
    if gols_inter > gols_gremio:
        vitorias_inter += 1
    elif gols_gremio > gols_inter:
        vitorias_gremio += 1
    else:
        empates += 1

    print('Novo grenal (1-sim 2-nao)')
    opcao = input()

print('%d grenais' % (vitorias_inter + vitorias_gremio + empates))
print('Inter:%d' % vitorias_inter)
print('Gremio:%d' % vitorias_gremio)
print('Empates:%d' % empates)

if vitorias_inter > vitorias_gremio:
    mensagem = 'Inter venceu mais'
elif vitorias_inter < vitorias_gremio:
    mensagem = 'Gremio venceu mais'
else:
    mensagem = 'Nao houve vencedor'

print(mensagem)
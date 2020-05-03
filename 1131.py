vitoria_gremio = 0
empates = 0
vitoria_inter = 0
grenais = 0
resposta = 1

while resposta == 1:
    gols_inter, gols_gremio = list(map(int, input().split(' ')))

    if gols_inter > gols_gremio:
        vitoria_inter += 1
    elif gols_gremio > gols_inter:
        vitoria_gremio += 1
    else:
        empates += 1
    grenais += 1
    print('Novo grenal (1-sim 2-nao)')
    resposta = int(input())

print('{0} grenais'.format(grenais))
print('Inter:{0}'.format(vitoria_inter))
print('Gremio:{0}'.format(vitoria_gremio))
print('Empates:{0}'.format(empates))

if vitoria_inter > vitoria_gremio:
    print('Inter venceu mais')
elif vitoria_gremio > vitoria_inter:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')
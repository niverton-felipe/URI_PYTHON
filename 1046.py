hora_inicio, hora_final = list(map(int, input().split()))

if (hora_final > hora_inicio):
    duracao = hora_final - hora_inicio
elif (hora_final == hora_inicio):
    duracao = 24
else:
    restante = 24 - hora_inicio
    duracao = hora_final + restante

print('O JOGO DUROU {0} HORA(S)'.format(duracao))
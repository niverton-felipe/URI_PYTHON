hora_inicial, minuto_inicial, hora_final, minuto_final = list(map(int, input().split()))

if hora_inicial == hora_final and minuto_inicial == minuto_final:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    if hora_inicial == hora_final and minuto_inicial > minuto_final:
        hora_final += 23
        minuto_final += 60
    
    elif hora_inicial < hora_final and minuto_inicial > minuto_final:
        hora_final -= 1
        minuto_final += 60

    elif hora_inicial > hora_final:        
        if minuto_inicial < minuto_final:
            hora_final += 24
        else:
            hora_final += 23
            minuto_final += 60
    
    hora_total = hora_final - hora_inicial
    minuto_total = minuto_final - minuto_inicial
    print('O JOGO DUROU {0} HORA(S) E {1} MINUTO(S)'.format(hora_total, minuto_total))
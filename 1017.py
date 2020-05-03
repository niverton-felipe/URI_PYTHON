tempo_gasto = int(input())
vel_media = int(input())
distancia = vel_media * tempo_gasto
qtd_combustivel_litro = 12

qtd_necessaria = distancia / qtd_combustivel_litro

print('{:.3f}'.format(qtd_necessaria))
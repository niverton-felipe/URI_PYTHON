import math

x1,y1 = list(map(float, input().split(" ")))
x2,y2 = list(map(float, input().split(" ")))

resultado = (x2 - x1) ** 2 + (y2 - y1) ** 2
distancia = math.sqrt(resultado)

print('{:.4f}'.format(distancia))
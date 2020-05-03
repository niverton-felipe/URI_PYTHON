import math

A, B, C = list(map(float, input().split(' ')))

delta = B ** 2 - (4 * A * C)

if delta < 0 or (2 * A == 0):
    print('Impossivel calcular')
else:
    x1 = (-B + math.sqrt(delta)) / (2 * A)
    x2 = (-B - math.sqrt(delta)) / (2 * A)
    print('R1 = {0:.5f}'.format(x1))
    print('R2 = {0:.5f}'.format(x2))
print('')


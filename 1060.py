cont = 0
positivo = 0

while cont <= 5:
    numero = float(input())
    cont += 1
    if numero > 0:
        positivo += 1

print('{0} valores positivos'.format(positivo))
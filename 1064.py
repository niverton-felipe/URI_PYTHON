soma = 0
positivo = 0
cont = 0

while cont <= 5:
    numero = float(input())
    
    if numero > 0:
        positivo += 1
        soma += numero
    cont += 1

media = soma / positivo

print('{0} valores positivos'.format(positivo))
print('{0:.1f}'.format(media))
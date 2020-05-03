cont = 0
par = 0

while cont <= 4:
    numero = int(input())

    if  numero % 2 == 0:
        par += 1
    cont += 1

print('{0} valores pares'.format(par))

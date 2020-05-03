casos = int(input())
dentro = 0
fora = 0
cont = 0

while casos > cont:
    numero = int(input())
    if 10 <= numero <= 20:
        dentro += 1
    else:
        fora += 1
    cont += 1
print('{0} in'.format(dentro))
print('{0} out'.format(fora))
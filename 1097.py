maior = 7
menor = 4

for i in range(1, 10, 2) :
    for j in range (maior, menor, - 1):
        print('I={} J={}'.format(i, j))
    maior += 2
    menor += 2
ladoA, ladoB, ladoC = list(map(float, input().split(' ')))

maior = 0
menor = 0
intermediario = 0

if ladoA > ladoB and ladoA > ladoC:
    maior = ladoA
elif ladoB > ladoA and ladoB > ladoC:
    maior = ladoB
else:
    maior = ladoC

if ladoA < ladoB and ladoA < ladoC:
    menor = ladoA
elif ladoB < ladoA and ladoB < ladoC:
    menor = ladoB
else:
    menor = ladoC

if ladoA != maior and ladoA != menor:
    intermediario = ladoA
elif ladoB != maior and ladoB != menor:
    intermediario = ladoB
else:
    intermediario = ladoC

triangulo = maior < (intermediario + menor)

if triangulo:
    perimetro = ladoA + ladoB + ladoC
    print('Perimetro = {0:.1f}'.format(perimetro))
else:
    area = ((ladoA + ladoB) * ladoC) / 2
    print('Area = {0:.1f}'.format(area))

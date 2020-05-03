ladoA, ladoB, ladoC = list(map(float, input().split(" ")))
pi = 3.14159

area_triangulo = (ladoA * ladoC) / 2
area_circulo = (ladoC ** 2) * pi
area_trapezio = ((ladoA + ladoB) * ladoC) / 2
area_quadrado = ladoB * ladoB
area_retangulo = ladoA * ladoB

print('TRIANGULO: {:.3f}'.format(area_triangulo))
print('CIRCULO: {:.3f}'.format(area_circulo))
print('TRAPEZIO: {:.3f}'.format(area_trapezio))
print('QUADRADO: {:.3f}'.format(area_quadrado))
print('RETANGULO: {:.3f}'.format(area_retangulo))
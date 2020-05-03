maior = 0

for pos in range(1, 101):
    numero = int(input())
    if numero > maior :
        maior = numero
        pos_maior = pos
print(maior)
print(pos_maior)
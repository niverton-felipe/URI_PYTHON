cont = 0

numeros = []

testes = int(input())

while cont < testes:
    numeros.append(int(input()))    
    cont += 1

for numero in numeros:
    if numero == 0:
        print('NULL')
    elif numero % 2 == 0:
        if numero > 0:
            print('EVEN POSITIVE')
        else:
            print('EVEN NEGATIVE')
    else:
        if numero > 0:
            print('ODD POSITIVE')
        else:
            print('ODD NEGATIVE')
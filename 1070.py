numero = int(input())

cont = 0

if numero % 2 == 0:
    numero += 1

while cont <= 5:    
    print(numero)
    numero += 2
    cont +=1
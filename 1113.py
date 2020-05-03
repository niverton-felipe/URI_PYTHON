numeros_diferentes = True

while numeros_diferentes :
    numero1, numero2 = list(map(int, input().split(' ')))
    if numero1 > numero2 :
        print('Decrescente')
    elif numero2 > numero1 :
        print('Crescente')
    else :
        numeros_diferentes = False
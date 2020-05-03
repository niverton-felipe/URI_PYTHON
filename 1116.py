testes = int(input())

for n in range(testes) :
    numero1, numero2 = list(map(int, input().split(' ')))
    if numero2 == 0 :
        print('divisao impossivel')

    else :
        resultado = numero1 / numero2
        print('{:.1f}'.format(resultado))
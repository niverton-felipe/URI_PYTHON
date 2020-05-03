numero1, numero2, numero3 = list(map(float, input().split()))

if numero2 <= numero1 >= numero3:
    A = numero1

    if numero2 >= numero3:
        B = numero2
        C = numero3
    else:
        B = numero3
        C = numero2

elif numero1 < numero2 >= numero3:
    A = numero2

    if numero1 >= numero3:
        B = numero1
        C = numero3
    else:
        B = numero3
        C = numero1

else:
    A = numero3

    if numero1 >= numero2:
        B = numero1
        C = numero2
    else:
        B = numero2
        C = numero1

if A >= B + C:
    print('NAO FORMA TRIANGULO')

elif (A ** 2) == (B ** 2) + (C ** 2):
    print('TRIANGULO RETANGULO')
    if A == B or A == C or B == C:
        print('TRIANGULO ISOSCELES')
    

elif A ** 2 > (B ** 2) + (C ** 2):
    print('TRIANGULO OBTUSANGULO')
    if A == B or A == C or B == C:
        print('TRIANGULO ISOSCELES')
    

elif A ** 2 < (B ** 2) + (C ** 2):
    print('TRIANGULO ACUTANGULO')
    if A == B == C:
        print('TRIANGULO EQUILATERO')
    elif A == B or A == C or B == C:
        print('TRIANGULO ISOSCELES')

elif A == B == C:
    print('TRIANGULO EQUILATERO')

elif A == B or A == C or B == C:
    print('TRIANGULO ISOSCELES')

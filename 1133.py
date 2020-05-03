numero1 = int(input())
numero2 = int(input())

if numero2 >= numero1 :
    for n in range(numero1 + 1, numero2) :
        if n % 5 == 2 or n % 5 == 3 :
            print(n)

if numero1 > numero2 :
    for n in range(numero2 + 1, numero1) :
        if n % 5 == 2 or n % 5 == 3:
            print(n)
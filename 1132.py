numero1 = int(input())
numero2 = int(input())
total = 0

if numero2 >= numero1 :
    for n in range(numero1, numero2 + 1) :
        if n % 13 != 0:
            total += n
else:
    for n in range(numero2, numero1 + 1) :
        if n % 13 != 0:
            total += n
print(total)
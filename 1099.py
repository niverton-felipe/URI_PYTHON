testes = int(input())

for c in range(testes) :
    num1, num2 = list(map(int, input().split(' ')))
    total = 0
    if num1 >= num2 :
        for impar in range(num1 - 1, num2, - 1) :
            if impar % 2 != 0 :
                total += impar
    else :
        for impar in range(num1 + 1, num2, 1):
            if impar % 2 != 0:
                total += impar
    print(total)
num1, num2, num3 = list(map(int, input().split(" ")))
maiorAB = 0
MAIOR = 0

if num1 > num2:
    maiorAB = num1
else:
    maiorAB = num2

if maiorAB > num3:
    MAIOR = maiorAB
else:
    MAIOR = num3
print('{0} eh o maior'.format(MAIOR))
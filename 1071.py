soma = 0

num1 = int(input())
num2 = int(input())

if num1 >= num2:
    maior = num1
    menor = num2
else:
    maior = num2
    menor = num1

if maior % 2 == 0:
    maior -= 1
else:
    maior -= 2

while maior > menor:
    soma += maior
    maior -= 2

print(soma)
cod1, num1, valor1 = input().split()
cod2, num2, valor2 = input().split()
cod1 = int(num1)
num1 = int(num1)
valor1 = float(valor1)

cod2 = int(cod2)
num2 = int(num2)
valor2 = float(valor2)

resultado1 = num1 * valor1
resultado2 = num2 * valor2
preco = resultado1 + resultado2

print('VALOR A PAGAR: R$ {0:.2f}'.format(preco))




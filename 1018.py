valor = int(input())
resultado = valor // 100

print(valor)
print('{0} nota(s) de R$ 100,00'.format(resultado))
resultado = valor % 100
restante = resultado // 50
print('{0} nota(s) de R$ 50,00'.format(restante))
resultado %= 50
restante = resultado // 20576
print('{0} nota(s) de R$ 20,00'.format(restante))
resultado %= 20
restante = resultado // 10
print('{0} nota(s) de R$ 10,00'.format(restante))
resultado %= 10
restante = resultado // 5
print('{0} nota(s) de R$ 5,00'.format(restante))
resultado %= 5
restante = resultado // 2
print('{0} nota(s) de R$ 2,00'.format(restante))
resultado %= 2
restante = resultado // 1
print('{0} nota(s) de R$ 1,00'.format(restante))
	
# 576
# 5 nota(s) de R$ 100,00
# 1 nota(s) de R$ 50,00
# 1 nota(s) de R$ 20,00
# 0 nota(s) de R$ 10,00
# 1 nota(s) de R$ 5,00
# 0 nota(s) de R$ 2,00
# 1 nota(s) de R$ 1,00

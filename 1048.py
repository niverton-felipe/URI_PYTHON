salario = float(input())

if salario <= 400:
    percentual = 15
    novo_salario = salario + (salario * (percentual / 100))
    reajuste = novo_salario - salario

elif 400 < salario <= 800:
    percentual = 12
    novo_salario = salario + (salario * (percentual / 100))
    reajuste = novo_salario - salario

elif 800 < salario <= 1200:
    percentual = 10
    novo_salario = salario + (salario * (percentual / 100))
    reajuste = novo_salario - salario

elif 1200 < salario <= 2000:
    percentual = 7
    novo_salario = salario + (salario * (percentual / 100))
    reajuste = novo_salario - salario

elif salario > 2000:
    percentual = 4
    novo_salario = salario + (salario * (percentual / 100))
    reajuste = novo_salario - salario

print('Novo salario: {0:.2f}'.format(novo_salario))
print('Reajuste ganho: {0:.2f}'.format(reajuste))
print('Em percentual: {0} %'.format(percentual))

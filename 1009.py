nome =str(input())
salario = float(input())
vendas = float(input())
taxa = 0.15
comissao = vendas * taxa
salario_total = salario + comissao
print('TOTAL = R$ {0:.2f}'.format(salario_total))

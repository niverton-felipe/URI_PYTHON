dias = int(input())

ano = dias // 365
restante = dias % 365
mes = restante // 30
dia = restante % 30

print('{0} ano(s)'.format(ano))
print('{0} mes(es)'.format(mes))
print('{0} dia(s)'.format(dia))
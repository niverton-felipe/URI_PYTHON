testes = int(input())

tot_coelhos = 0
tot_sapos = 0
tot_ratos = 0
tot_cobaias = 0

for c in range(testes) :
    quantidade, especie = list(map(str, input().split(' ')))
    if especie == 'C' :
        tot_coelhos += int(quantidade)
    elif especie == 'S':
        tot_sapos += int(quantidade)
    elif especie == 'R' :
        tot_ratos += int(quantidade)
    tot_cobaias += int(quantidade)

percentual_coelhos = (tot_coelhos / tot_cobaias) * 100
percentual_ratos = (tot_ratos/ tot_cobaias) * 100
percentual_sapos = (tot_sapos / tot_cobaias) * 100

print('Total: {} cobaias'.format(tot_cobaias))
print('Total de coelhos: {}'.format(tot_coelhos))
print('Total de ratos: {}'.format(tot_ratos))
print('Total de sapos: {}'.format(tot_sapos))
print('Percentual de coelhos: {:.2f} %'.format(percentual_coelhos))
print('Percentual de ratos: {:.2f} %' .format(percentual_ratos))
print('Percentual de sapos: {:.2f} %'.format(percentual_sapos))

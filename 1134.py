tot_gasolina = 0
tot_alcool = 0
tot_diesel = 0
resp = 0

while resp != 4 :
    resp = int(input())
    if resp == 1:
        tot_alcool += 1
    elif resp == 2:
        tot_gasolina += 1
    elif resp == 3:
        tot_diesel += 1
print('MUITO OBRIGADO')
print('Alcool: {}'.format(tot_alcool))
print('Gasolina: {}'.format(tot_gasolina))
print('Diesel: {}'.format(tot_diesel))

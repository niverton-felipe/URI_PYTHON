salario = float(input())
controle = 2000
imposto = 0

if salario <= controle:
    print('Isento')
else:
    salario -= controle
    
    if salario <= 1000:
        imposto = salario * 0.08
        print('R$ {0:.2f}'.format(imposto))
    elif  1000 < salario <= 2500:
        imposto = 80
        salario -= 1000
        imposto += (salario * 0.18)
        print('R$ {0:.2f}'.format(imposto))
    else:
        imposto = 350
        salario -= 2500
        imposto += (salario * 0.28)
        print('R$ {0:.2f}'.format(imposto))




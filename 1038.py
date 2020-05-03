codigo, quantidade = list(map(int, input().split(' ')))

preco = 0

if codigo == 1:
    preco = 4 * quantidade
    print('Total: R$ {0:.2f}'.format(preco))
elif codigo == 2:
    preco = 4.5 * quantidade
    print('Total: R$ {0:.2f}'.format(preco))
elif codigo == 3:
    preco = 5.0 * quantidade
    print('Total: R$ {0:.2f}'.format(preco))
elif codigo == 4:
    preco = 2.0 * quantidade
    print('Total: R$ {0:.2f}'.format(preco))
else:
    preco = 1.5 * quantidade    
    print('Total: R$ {0:.2f}'.format(preco))
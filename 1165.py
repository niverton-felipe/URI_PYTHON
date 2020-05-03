testes = int(input())
cont = 0

while cont < testes:
    numero = int(input())
    if numero % 2 == 0:
        if numero == 2:
            print('{} eh primo'.format(numero))
        else:
            print('{} nao eh primo'.format(numero))
    
    else:
        div = 3
        contador = 0
        while div <= numero ** 0.5 and contador == 0:
            if numero % div == 0:
                contador += 1
            div += 2
        
        if contador == 0 :
            print('{} eh primo'.format(numero))
        else:
            print('{} nao eh primo'.format(numero))  
    
    cont += 1

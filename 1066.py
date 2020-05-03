par = 0
impar = 0
positivo = 0
negativo = 0
cont = 0

while cont <= 4:
    numero = int(input())

    if numero % 2 == 0:
        par += 1
    else:
        impar +=1
    
    if numero > 0:
        positivo += 1
    elif numero < 0:
        negativo += 1

    cont += 1
    
print('{0} valor(es) par(es)'.format(par))
print('{0} valor(es) impar(es)'.format(impar))
print('{0} valor(es) positivo(s)'.format(positivo))
print('{0} valor(es) negativo(s)'.format(negativo))
cont = 0
soma = 0

while cont < 2:
    nota = float(input())

    if  nota > 10 or nota < 0:
        print('nota invalida')
    else:
        soma += nota
        cont += 1
media = soma / 2
print('media = {0:.2f}'.format(media))
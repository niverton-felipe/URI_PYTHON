resposta = 1

while resposta == 1:
    
    cont = 0
    soma = 0
    auxiliar = 0

    while cont < 2:
        nota = float(input())
        if 10 >= nota >= 0:
            soma += nota
            cont += 1
        else:
            print('nota invalida')

    media = soma / 2
    print('media = {0:.2f}'.format(media)) 

    while auxiliar not in (1, 2):
        print('novo calculo (1-sim 2-nao)')
        auxiliar = int(input())
    resposta = auxiliar
 
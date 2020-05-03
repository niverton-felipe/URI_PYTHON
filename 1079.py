testes = int(input())

for n in range(testes) :
    nota1, nota2, nota3 = list(map(float, input().split(' ')))
    media_ponderada = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10
    print('{0:.1f}'.format(media_ponderada))
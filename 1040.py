nota1, nota2, nota3, nota4 = list(map(float, input().split(' ')))

media_regular = ((nota1 * 2) + (nota2 * 3) + (nota3 * 4) + (nota4 * 1)) / 10

if media_regular >= 7.0 :
    print('Media: {0:.1f}'.format(media_regular))
    print('Aluno aprovado.')

elif 5.0 <= media_regular <= 6.9:
    print('Media: {0:.1f}'.format(media_regular))
    print('Aluno em exame.')
    nota_exame = float(input())
    media_final = (media_regular + nota_exame) / 2
    print('Nota do exame: {0:.1f}'.format(nota_exame))
    if media_final >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: {0:.1f}'.format(media_final))
else:
    print('Media: {0:.1f}'.format(media_regular))
    print('Aluno reprovado.')
classificacao_um =  input()
classificacao_dois = input()
classificacao_tres = input()

if classificacao_um == 'vertebrado':
    if classificacao_dois == 'ave':
        if classificacao_tres == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if classificacao_tres == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if classificacao_dois == 'inseto':
        if classificacao_tres == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if classificacao_tres == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')

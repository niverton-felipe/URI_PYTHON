x = 1
y = 1

while x or y != 0:
    x, y = list(map(int, input().split()))

    if x > 0:
        if y > 0:
            print('primeiro')
        else:
            print('quarto')
    elif x < 0:
        if y > 0:
            print('segundo')
        else:
            print('terceiro')
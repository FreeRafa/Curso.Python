while True:
    print('=='*20)
    n = int(input('De qual número você quer ver a tabuada? '))
    if n < 0:
        print('Este valor termina o programa')
        break
    for c in range(1, 11):
        print(f'{n} X {c} = {n*c}')

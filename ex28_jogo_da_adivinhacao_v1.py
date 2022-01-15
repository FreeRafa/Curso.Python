from random import randint
num = randint(0, 5)
#print('Pensei no numero ...{}'.format(num))

jogador = int(input('Em que numero eu pensei?'))
if jogador == num:
    print('Parabens você acertou')
else:
    print('Você errou, eu pensei no numero {} e nao no numero {}'.format(num, jogador))


from random import randint

tot = 0
computador = randint(1, 6)
jogador = int(input('O numero que você pensou é: '))

while computador != jogador:
    print('ERROU! tente outra vez')
    computador = int(input('Em que numero eu pensei de novo? '))
    tot += 1
    if jogador > computador:
        print('Mais... Tente mais uma vez!')
    elif jogador < computador:
        print('Menos ... Tente mais uma vez!')
if computador == jogador:
    print('PARABENS você acertou ')
print('O número de tentativas foi de {}'.format(tot))


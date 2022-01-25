import random
from random import randint

print('-=-'*20)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=-'*20)
v = 0

while True:
    jogador = int(input('Digite um numero: '))
    computador = random.randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogo {jogador} e o computador jogou {computador}. E um total de {total}', end='')
    print('DEU PAR' if total % 2 == 0 else ' DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('você VENCEU!!')
            v += 1
        else:
            print('Você PERDEU!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce VENCEU!!')
            v += 1
        else:
            print('Você PERDEU!!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! você venceu {v} vezes!')


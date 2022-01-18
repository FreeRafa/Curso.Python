soma = 0
cont = 0
for c in range(1, 7):
    n1 = int(input('Digite o {} número inteiro: '.format(c)))
    if n1 % 2 == 0:
        soma = soma + n1
        cont = cont + 1
print('Você informou {} números pares e a soma deles é {}'.format(cont, soma))


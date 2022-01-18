maiorpeso = 0
menorpeso = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {} pessoa:'.format(c)))
    if c == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso

print('O maior peso da lista é {}Kg'.format(maiorpeso))
print('O menor peso da lista é {}Kg'.format(menorpeso))

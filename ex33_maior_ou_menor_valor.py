num1 = int(input('Digite um valor'))
num2 = int(input('Digite um segundo valor'))
num3 = int(input('Digite um terceiro valor'))

maior = num1
if num2 > num3 and num2 > num1:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

print('O maior numero é {}'.format(maior))
print('O menor numero é {}'.format(menor))



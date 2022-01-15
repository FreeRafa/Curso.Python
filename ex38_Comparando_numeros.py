#Comparando dois números

num1 = int(input('Digite um número qualquer:'))
num2 = int(input('Digite um segundo número qualquer:'))

if num1 == num2:
    print('Os números {}, e {}, são iguais'.format(num1, num2))
elif num1 > num2:
    print('O primeiro número {} é MAIOR, que o segundo número {}'.format(num1, num2))
elif num1 < num2:
    print('O primeiro número {} é MENOR, que o segundo número {}'.format(num1, num2))



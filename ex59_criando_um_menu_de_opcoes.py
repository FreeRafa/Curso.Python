import math
from math import sqrt
from math import sin, cos, tan, pow, factorial

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

opcao = 0
soma = 0
multiplicacao = 0
media = 0
raizn1 = 0
raizn2 = 0
sinn1 = 0
cosn1 = 0
tann1 = 0
sinn2 = 0
cosn2 = 0
tann2 = 0
potn = 0
facn1 = 0
facn2 = 0

while opcao != 10:
      print('''
      [ 1 ] SOMAR
      [ 2 ] MULTIPLICAR
      [ 3 ] MAIOR
      [ 4 ] OUTROS NÚMEROS
      [ 5 ] MÉDIA
      [ 6 ] RAIZ QUADRADA
      [ 7 ] SENO, COSENO E TANGENTE
      [ 8 ] POTÊNCIA 
      [ 9 ] FATORIAL
      [ 10 ] FIM DO PROGRAMA''')
      opcao = int(input('Qual a sua opção: '))
      print('=='*30)
      if opcao == 1:
            soma = n1 + n2
            print('A soma de {}, mais {}, é {}'.format(n1, n2, soma))

      if opcao == 2:
            multiplicacao = n1 * n2
            print('A multiplicação entre {}, e {} é {}'.format(n1, n2, multiplicacao))

      if opcao == 3:
            if n1 > n2:
                  print('O {} é maior'.format(n1))
            else:
                  print('O número {} é menor'.format(n2))

      if opcao == 4:
            n1 = int(input('Digite outro número: '))
            n2 = int(input('Digite mais um número: '))
            print('O que você pretente fazer com este números? ')
            print(opcao)

      if opcao == 5:
            media = (n1 + n2) / 2
            print('A média entre {} e {} é {:.1f}'.format(n1, n2, media))

      if opcao == 6:
            raizn1 = math.sqrt(n1)
            print('A rais quadrada de {}  é {:.2f}'.format(n1, raizn1))
            raizn2 = math.sqrt(n2)
            print('A raiz quadrada de {} é {}'.format(n2, raizn2))

      if opcao == 7:
            sinn1 = math.sin(n1)
            cosn1 = math.cos(n1)
            tann1 = math.tan(n1)
            print('O seno de {} é {:.2f}\nO coseno é {:.2f}\ne a tangente é {:.2f}'.format(n1,sinn1, cosn1, tann1))
            sinn2 = math.sin(n2)
            cosn2 = math.cos(n2)
            tann2 = math.tan(n2)
            print('O seno de {} é {:.2f}\nO coseno é {:.2f}\ne a tangente é {:.2f}'.format(n2, sinn2, cosn2, tann2))

      if opcao == 8:
            potn = math.pow(n1, n2)
            print('O número {} elevado a potência do número {} é {}'.format(n1, n2, potn))

      if opcao == 9:
            facn1 = math.factorial(n1)
            print('O Valor fatorial de {} é {}'.format(n1, facn1))
            facn2 = math.factorial(n2)
            print('O valor fatoria de {} é {}'.format(n2, facn2))

      if opcao >= 11:
            print('OPÇÃO INVALIDA\nO QUE DESEJA FAZER? ')

      if opcao == 10:
            print('OBRIGADO POR USAR NOSSO APP')




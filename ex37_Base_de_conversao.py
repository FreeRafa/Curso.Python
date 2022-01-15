n1 = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases de conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção:'))

if opcao == 1:
    print('{} convertido para BINÁRIO é {}'.format(n1, bin(n1)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é {}'.format(n1, oct(n1)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(n1, hex(n1)[2:]))
else:
    print('Opção invalida. Tente Novamente')

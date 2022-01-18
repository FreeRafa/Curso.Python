frase = str(input('Digite uma frase :')).strip().upper() #o lobo ama o bolo
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) - 1, - 1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Esta frase é um PALINDROMO')
else:
    print('Esta frase NÃO É UM PALINDROMO' )


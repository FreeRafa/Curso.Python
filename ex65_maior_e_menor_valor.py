from time import sleep
resp = 'Ss'
n = 0
media = 0
maior = -999
menor = 999
soma = 0
tot = 0
while resp in 'Ss':
    n = int(input('Digite um numero: '))
    resp = str(input('Deseja continuar [S/N] ')).upper().strip()[0]
    soma = soma + n
    tot = n
    media = soma / tot
    if n > maior:
        maior = n
    if n < menor:
        menor = n


print('ANALIZANDO DADOS...')
sleep(2)
print('=='*20)
print('A MEDIA do total de números somados é {:.2f}'.format(media))
print('O TOTAL de números digitados foi {}'.format(tot))
print('A SOMA dos números digitados é {}'.format(soma))
print('O MAIOR número digitado foi {}'.format(maior))
print('O MENOR número digitado foi {}'. format(menor))
print('=='*20)
print('FIM')
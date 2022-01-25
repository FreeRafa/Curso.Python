quat = 0
soma = 0
while True:
    n = int(input('Digite um número inteiro:'))
    if n == 999:
        break
    quat = n
    soma = soma + n

print(f'A quantidade de números digitados foi {quat}')
print(f'E a soma de todos os números digitados foi {soma}')

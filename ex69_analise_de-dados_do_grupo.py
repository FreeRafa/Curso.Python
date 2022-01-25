
pessoas18 = 0
homens = 0
mulheres = 0
while True:
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO: [M/F]')).upper().strip()[0]

    if idade >= 18:
        pessoas18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar cadastrando? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break

print('ACABOU')

print('-=-'*20)
print(f'A quantidade de pessoas maior de 18 anos é {pessoas18}')
print(f'A quantidade de homens cadastrados foi {homens}')
print(f'A quantidade de mulheres com menos de 20 anos é {mulheres}')

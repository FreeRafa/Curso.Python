sexo = str(input('Digite seu sex0 [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos.Por favor, digite seu sexo [M/F]:')).strip().upper()[0]
print('Dados cadastrados com sucesso, seco {}'.format(sexo))



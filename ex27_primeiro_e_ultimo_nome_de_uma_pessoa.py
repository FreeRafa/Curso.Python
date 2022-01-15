nome = str(input('digite seu nome completo:')).strip()
separa = nome.split()
print('Seu primeiro nome é {}'.format(separa[0]))
print('E seu ultimo nome é {}'.format(separa[len(separa)-1]))



nome = str(input('Digite seu nome e sobrenome:')).strip()
print('Analizando seu nome...')
print('Seu nome em letras maiusculas é {}'.format(nome.upper()))
print('Seu nome em letras minusculas é {}'.format(nome.lower()))
print('Seu nome tem {}'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e seu ultimo nome é {} e ele tem {} letras'.format(separa[0], separa[2], len(separa[0])))


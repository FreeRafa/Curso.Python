from itertools import count

frase = str(input('Digite uma frase:')).upper().strip()
print('a letra a apareceu {}'.format(frase.count('A')))
print('Em que posição ela aparece primeiro {}'.format(frase.find('A')+1))
print('Em que posição ela aparece pela ultima vez {}'.format(frase.rfind('A')+1))


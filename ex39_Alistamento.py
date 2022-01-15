#Definir quanto tempo falta para o alistamento militar

from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc

print('Quem nasceu em {}, tem {} anos em {}'.format(nasc, idade, atual))

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    salto = 18 - idade
    print('Falta {} anos para o alistamento'.format(salto))
    ano = atual + salto
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    salto = idade - 18
    print('Você ja deveria ter se alistado há {} anos.'.format(salto))
    ano = atual - salto
    print('Seu alistamento foi em {}'.format(ano))


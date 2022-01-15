#Classificando atletas de natação

from datetime import date

atual = date.today().year
idade = int(input('Digite a sua data de nascimento: '))
nasc = atual - idade

if nasc <= 9:
    print('Você tem {},anos e pertence a categoria'.format(nasc))
    print('MIRIM')
elif nasc > 9 and nasc <= 14:
    print('Você tem {},anos e pertence a categoria'.format(nasc))
    print('INFANTIL')
elif nasc > 14 and nasc <= 19:
    print('Você tem {},anos e pertence a categoria'.format(nasc))
    print('JUNIOR')
elif nasc > 19 and nasc <= 20:
    print('Você tem {},anos e pertence a categoria'.format(nasc))
    print('SÊNIOR')
else:
    nasc > 20
    print('Você tem {},anos e pertence a categoria'.format(nasc))
    print('MASTER')

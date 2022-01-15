sal = float(input('Qual o valor do seu salario?'))
if sal >= 1250:
    sal2 = sal * 10 / 100
    print('Seu novo salario com reajuste de 10% é R${} reais'.format(sal2 + sal))
if sal <= 1250:
    sal2 = sal * 15 / 100
    print('Seu novo salario com reajuste de 15% é R${} reais'.format(sal2 + sal))

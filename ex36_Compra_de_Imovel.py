#Empréstimo Bancário

casa = float(input('Qual o valor total do imovel? R$ '))
sal = float(input('Qual o seu salario mensal? R$ '))
anos = int(input('Em quantos anos você quer pagar? '))
prestacao = casa / (anos * 12)
minimo = sal * 30 / 100

print('O valor total do imovel é: R${:.3f} Mil Reais'.format(casa))
print('O salario do comprador é R${:.3f} Reais'.format(sal))
print('O imovel será quitado em {} anos'.format(anos))
print('Para pagar a casa de R${:.3f} Mil Reais em {} anos'.format(casa, anos))
print('A prestação será de R${:.3f}'.format(prestacao))

if prestacao <= minimo:
    print('Seu empréstimo pode ser CONCEDIDO')
else:
    print('Emprestimo NEGADO')




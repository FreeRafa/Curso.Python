num = int(input('Qual a distancia da viagem em KM?'))
if num <= 200:
    print('O valor da viagem é de R${} Reais'.format(num * 0.50))
if num >= 200:
    print('O valor da viagem custará R${} Reais'.format(num * 0.45))

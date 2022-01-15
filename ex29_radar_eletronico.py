vel = float(input('Qual a velocidade do carro?'))
if vel >= 80:
    print('Você foi multado')
    print('Sua multa é de R${:.2f} Reais'.format((vel - 80) * 7))
else:
    print('Mantenha a velocidade baixa!')

#Calculando o IMC de uma pessoa.

a = float(input('Digite a sua altura? (m) '))
p = float(input('Digite o seu peso? (kg) '))

imc = p / (a ** 2)
print('O seu IMS é de {:.1f}'.format(imc))

if imc <= 18.5:
    print('Você está abaixo do peso ideal.')
elif imc >= 18.5 and imc < 25:
    print('Você está com o peso ideal.')
elif imc >= 25 and imc <= 30:
    print('Você está com sobrepeso')
elif imc >= 30 and imc <= 40:
    print('Você está obeso')
elif imc >= 40:
    print('Você está com obesidade morbida')






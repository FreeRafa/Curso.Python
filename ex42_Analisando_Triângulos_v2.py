#Analisando triângulos em EQUILÁTERO, ESCALENO e ISÓSCELES

r1 = float(input('Qual o valor da primeira reta? '))
r2 = float(input('Qual o valor da segunda reta? '))
r3 = float(input('Qual o valor da terceira reta? '))

if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r3:
    print('Os seguimentos acima, PODEM FORMAR um triângulo!')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os elementos acima NÃO PODEM formar triângulo!')
#Média do aluno 2.0

n1 = float(input('Digite o valor da primeira nota: '))
n2 = float(input('Digite o valor da segunda nota: '))

media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))

if media < 5.0:
    print('Sua média foi de {:.1f}'.format(media))
    print('REPROVADO')
elif media == 5.0 or media <= 6.9:
    print('Sua média foi de {:.1f}'.format(media))
    print('RECUPERAÇÃO')
elif media >= 7.0:
    print('Sua média foi de {:.1f}'.format(media))
    print('APROVADO')

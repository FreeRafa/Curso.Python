total = 0
totmil = 0
menor = 0
cont = 0
barato = ' '

while True:
    produto = str(input('Produto: '))
    preco = float(input('Preço R$'))
    cont += 1

    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi de {total}')
print(f'Temos um total de {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi de {barato} que custa R${menor}')

#Tabuada de qualquer número V2.0

n1 = int(input('Digite o numero que você queira saber a tabuada: '))
print('=='*7)
for c in range(1, 11):
    print('{} x {} = {}'.format(n1, c, n1*c))
print('=='*7)
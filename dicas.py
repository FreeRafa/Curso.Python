from itertools import count

frase = 'Curso em Video Python'
frase2 = '    curso em     video   python    '
print(frase)
print(len(frase))
print(frase.find('o'))
print(frase.replace('Python', 'RAFAEL'))
print(frase.upper()) #Trasforma a frase todas em maiusculas
print(frase.lower()) #Trasforma a frase toda em minusculas
print(frase.lower().capitalize())
print(frase.title())
#print(frase2.strip()) nao entendi muito bem como funciona
print('*'.join(frase))
print('Curso' in frase) #Verifica se existe uma determinada palavra dentro da string (OBS:. palavra dever ser igual a da string)
print(frase.lower().find('curso'))
print(frase.split())

print('{:=^40}'.format(' EXERCÍCIO 53 '))

frase = input('Digite uma frase: ').strip().replace(' ', '').upper()
inverso = ''
'''for i in range(len(frase)-1, -1, -1):
    inverso += frase[i]'''
inverso = frase[::-1]
print(f'O inverso de {frase} é {inverso} ')
if frase == inverso:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada NÃO é um palíndromo!')

print(f'{" EXERCÍCIO 61 ":=^40}')

# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro
# termo e a razão de uma PA, mostrando os 10 primeiros termos
# da progressão usando a estrutura while.


print('-=' * 10)
p1 = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 0

while cont < 10:
    print(p1, end=' \u2192 ') #Usando unicode seta
    p1 += razao
    cont += 1
print('FIM')

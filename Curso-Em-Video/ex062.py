print(f'{" EXERCÍCIO 62 ":=^40}')

# Exercício Python 62: Melhore o DESAFIO 61,
# perguntando para o usuário se ele quer mostrar
# mais alguns termos. O programa encerrará quando
# ele disser que quer mostrar 0 termos.

print('-=' * 10)
p1 = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termos = 10 # Quantidade cumulativa de termos gerados
termosDesejados = 10 # Quantidades de termos a serem gerados

while termosDesejados > 0:
    print(p1, end=' \u2192 ') #Usando unicode seta
    p1 += razao
    if termosDesejados == 1:
        print('PAUSA')
        termosDesejados += int(input('Quantos termos você quer mostrar a mais? ').strip())
        termos += termosDesejados - 1
    termosDesejados -= 1

print(f'Progressão finalizada com {termos} termos mostrados.')

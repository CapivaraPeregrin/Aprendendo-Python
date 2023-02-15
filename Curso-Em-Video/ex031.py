print('====== EXERCÍCIO 31 ======')

# Exercício Python 31: Desenvolva um programa que pergunte a distância
# de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
# Km para viagens de até 200Km e R$0,45 parta viagens mais longas.


distancia = float(input('Qual a distância de sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}Km.'.format(distancia))
custo = 0.0
if distancia <= 200:
    custo = 0.5 * distancia
else:
    custo = 0.45 * distancia
print('E o preço da sua passagem será de R${:.2f}'.format(custo))

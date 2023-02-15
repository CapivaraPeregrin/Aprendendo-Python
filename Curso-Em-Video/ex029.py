print('====== EXERCÍCIO 29 ======')

# Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

RED = "\033[1;31m"
YELLOW = "\033[1;33m"
GREEN = "\033[0;32m"

velocidadeAtual = int(input('Qual a velocidade atual do carro? '))
if velocidadeAtual > 80:
    multa = float((velocidadeAtual - 80) * 7)
    print(RED + 'MULTADO! Você excedeu o limite permitido que é de 80km/h'
                '\nVocê deve pagar a multa de' + YELLOW + ' R${:.2f}'.format(multa))
print(GREEN + 'Tenha um bom dia! Dirija com segurança!')

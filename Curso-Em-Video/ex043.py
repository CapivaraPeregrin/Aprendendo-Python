print('====== EXERCÍCIO 43 ======')

# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura
# de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu
# status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

peso = float(input('Qual seu peso? (Kg) '))
altura = float(input('Qual sua altura? (m) '))

icm = peso / (altura**2)
print(f'O ICM dessa pessoa é de {icm:.1f}')
if icm < 18.5:
    print('Você está abaixo da faixa de peso normal.')
elif icm < 25:
    print('Parabéns, você está na faixa de peso normal.')
elif icm < 30:
    print('Você está em sobrepeso.')
elif icm < 40:
    print('Você está em obesidade.')
else:
    print('Você está em obsidade morbida, cuidado!')

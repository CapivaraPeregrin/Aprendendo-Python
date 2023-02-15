print('====== EXERCÍCIO 34 ======')

# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule
# o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = int(input('Qual é o salário do funcionário? R$'))
novoSalario = salario * 1.10 if salario > 1250 else salario * 1.15
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novoSalario))

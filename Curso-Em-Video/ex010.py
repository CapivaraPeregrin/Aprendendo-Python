print('====== EXERCÍCIO 10 ======')
#Exercício Python 10: Crie um programa que leia
# quanto dinheiro uma pessoa tem na carteira e mostre
# quantos dólares ela pode comprar.

carteira = float(input('Qual o valor em reais na sua carteira: '))
dolares = carteira/3.27
print('Em dólares você possui ${:.2f}'.format(dolares))

print(f'Em dólares você possui ${dolares:.2f}')

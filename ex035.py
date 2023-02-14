print('====== EXERCÍCIO 35 ======')

# Exercício Python 35: Desenvolva um programa que leia o comprimento
# de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

maior = max(s1, s2, s3)
if maior < (s1 + s2 + s3 - maior):
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')


#Aula 11
print('\033[7mOlá mundo! \033[m')
print('\033[4;30;43m Olá mundo! \033[m')


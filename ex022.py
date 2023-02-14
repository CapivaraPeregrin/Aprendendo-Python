#Aula 09
frase = 'Curso em vídeo python'
print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:]) # do 15 até o final
print(frase[9::3])

#Análise

print(len(frase))
print(frase.count('o'))
print(frase.count('z'))
print(frase.count('o', 0, 13))
print(frase.find('o'))
print(frase.find('android')) # retorna -1 quando não achado
"curso" in frase
frase.upper()
frase.lower()
frase.capitalize() # apenas a primeira letra da string
frase.title() # primeira letra de cada palavra

frase.replace('python', 'android')

frase.strip() #apaga espaços no inicio e fim
frase.rstrip()
frase.lstrip()

texto = frase.split()
'-'.join(texto)
print(frase)
print(texto)
print('-'.join(texto))

# Aspas duplas três vezes facilita o rin de grandes textos
print("""Nessa aula, vamos aprender operações com String no Python. 
As principais operações que vamos aprender são o Fatiamento de String,
Análise com len(), count(), find(), transformações com replace(), 
upper(), lower(), capitalize(), title(), strip(), junção com join().""")

print('====== EXERCÍCIO 22 ======')
#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras aotodo (sem considerar espaços)
# Quantas letras tem o primeiro nome.

nomeCompleto = input('Digite seu nome completo: ')
print('Analisando seu nome...')
nomeCompleto = nomeCompleto.strip()
print('Seu nome em maiúsculas é {}'.format(nomeCompleto.upper()))
print('Seu nome em minúsculas é {}'.format(nomeCompleto.lower()))
qtdeLetras = len(nomeCompleto)-nomeCompleto.count(' ')
print('Seu nome tem ao todo {} letras'.format(qtdeLetras))
print('Seu primeiro nome é {} e ele tem {} letras'.format(nomeCompleto.split()[0], len(nomeCompleto.split()[0])))

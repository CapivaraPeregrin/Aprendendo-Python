print(f'{" EXERCÍCIO 80 ":=^50}')

# Exercício Python 080: Crie um programa onde o usuário possa digitar
# cinco valores numéricos e cadastre-os em uma lista, já na posição
# correta de inserção (sem usar o sort()). No final, mostre a lista
# ordenada na tela.

numeros = []
for i in range(0, 5):
    num = (int(input('Digite um valor: ')))
    if i == 0:
        numeros.append(num)
        print('Adicionado na posição 0 da lista...')
    else:
        for j in range(0, len(numeros)):
            if num <= numeros[j]:
                numeros.insert(j, num)
                print(f'Adicionado na posição {j} da lista...')
                break
            elif num > max(numeros):
                numeros.append(num)
                print(f'Adicionado ao final da lista...')
                break

print('-=' * 25)
print(f'Os valores digitados em ordem foram {numeros}')

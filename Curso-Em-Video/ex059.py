from time import sleep

print('{:=^40}'.format(' EXERCÍCIO 59 '))

# Exercício Python 059: Crie um programa que leia dois valores e mostre
# um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

num1 = float(input('Primeiro valor: '))
num2 = float(input('Segundo valor: '))

opcao = 0
while opcao != 5:
    print('=-=' * 15)
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')

    opcao = int(input('>>>>> Qual é a sua opção? ').strip())

    if opcao == 1:
        print(f'A soma entre {num1} e {num2} é {num2+num1}')
    elif opcao == 2:
        print(f'O resultado de {num1} x {num2} é {num2*num1:.2f}')
    elif opcao == 3:
        maior = max([num2, num1])
        print(f'Entre {num1} e {num2} o maior valor é {maior}')
    elif opcao == 4:
        print('Informe os números novamente:')
        num1 = float(input('Primeiro valor: '))
        num2 = float(input('Segundo valor: '))
    elif opcao != 5:
        print('Opção inválida. Tente novamente')
    else:
        print('Finalizando...')
print('=-=' * 15)
sleep(1)
print('Fim do programa! Volte sempre')

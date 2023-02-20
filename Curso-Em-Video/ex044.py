print('====== EXERCÍCIO 44 ======')

# Exercício Python 44: Elabore um programa que calcule o valor a ser pago
# por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros
print('{:=^40}'.format(' LOJAS CAPIVARA '))

precoInicial = float(input('Preço das compras: R$'))

print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')

opcao = int(input('Qual sua opção? '))
valorFinal = 0
parcelas = 0
continuar = True

if opcao == 1:
    valorFinal = precoInicial * 0.9
elif opcao == 2:
    valorFinal = precoInicial * 0.95
elif opcao == 3:
    valorFinal = precoInicial
    valorParcela = valorFinal / 2
    print(f'Sua compra será parcelada em 2x de R${valorParcela:.2f} SEM JUROS')
elif opcao == 4:
    valorFinal = precoInicial * 1.2
    parcelas = int(input('Quantas parcelas? '))
    if parcelas <= 2:
        print('Valor Inválido!')
        continuar = False
    else:
        valorParcela = valorFinal / parcelas
        print(f'Sua compra será parcelada em {parcelas}x de R${valorParcela:.2f} COM JUROS')
else:
    print('OPÇÃO INVÁLIDA DE PAGAMENTO')
    continuar = False

if continuar:
    print(f'Sua compra de R${precoInicial:.2f} vais custar R${valorFinal:.2f} no final.')

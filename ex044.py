valor = float(input('Qual o valor da compra? R$'))

print('Qual a forma de pagamento?')
print('[1] Dinheiro')
print('[2] Cartão à vista')
print('[3] Cartão 2x')
print('[4] Cartão 3x ou mais')
fp = float(input(''))

if fp == 1:
    print(f'Parabens voce recebeu 10% de desconto por pagar no dinheiro')
    print(f'Sua compra de R${valor:.2f} vai sair por R${(valor - (valor*0.1)):.2f}')
elif fp == 2:
    print('Parabens voce recebeu 5% de desconto por pagar à vista')
    print(f'Sua compra de R${valor:.2f} vai sair por R${(valor - (valor * 0.05)):.2f}')
elif fp == 3:
    print(f'Voce pagará R${valor} em 2X no cartão')
elif fp == 4:
    print('Compras parceladas em 3X ou mais tem 20% de juros')
    print(f'Sua compra de R${valor:.2f} vai sair por R${(valor + (valor * 0.2)):.2f}')
else:
    print('Selecione uma opção válida')

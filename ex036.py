casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos voce pretende pagar essa casa? '))

parcela = casa / (anos * 12)
limite = salario * 0.3

if parcela >= limite:
    print('Pedido negado, infelizmente voce não pode parcelar essa casa')
else:
    print('Pedido aprovado, voce pode parcelar essa casa')

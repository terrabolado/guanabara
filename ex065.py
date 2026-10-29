cond = 'S'
soma = 0
lista = []
while cond == 'S':
    valor = int(input('Digite um numero - '))
    soma += valor
    lista.append(valor)
    cond = input('Deseja continuar? [S/N] ').upper().strip()[0]
media = soma / len(lista)
print(f'A média entre os valores digitados é de {media:.2f}. O maior numero foi {max(lista)} e o menor {min(lista)}.')

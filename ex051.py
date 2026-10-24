print('PROGRESSÃO ARITMÉTICA')
termo = int(input('Escolha o termo da progressão: '))
razao = int(input('Escolha a razão da progressão: '))
decimo = termo + (10 - 1) * razao
for i in range(termo, (decimo + razao), razao):
    print(i, end=' ')

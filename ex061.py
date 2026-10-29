print('PROGRESSÃO ARITMÉTICA')
termo = int(input('Escolha o termo da progressão: '))
razao = int(input('Escolha a razão da progressão: '))
pa = []
while len(pa) < 10:
    print(termo, end=' ')
    pa.append(termo)
    termo += razao
print()
print(*pa)
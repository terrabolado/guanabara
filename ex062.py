print('PROGRESSÃO ARITMÉTICA')
termo = int(input('Escolha o termo da progressão: '))
razao = int(input('Escolha a razão da progressão: '))
pa = []
while len(pa) < 10:
    print(termo, end=' ')
    pa.append(termo)
    termo += razao
print()
esc = int(input('Quantos outros termos voce deseja ver? '))
while esc != 0:
    nmr = termo + (esc - 1) * razao
    for i in range(termo, (nmr + razao), razao):
        print(i, end=' ')
        termo += razao
    print()
    esc = int(input('Quantos outros termos voce deseja ver? '))

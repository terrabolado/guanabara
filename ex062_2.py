from os import system
print('Progressão Aritmética')
termo = int(input('Insira o Termo: '))
razao = int(input('Insira a razão: '))
adc = 10
total = 0
pa = []
while adc != 0:
    total += adc
    while len(pa) < total:
        print(termo, end=' ')
        pa.append(termo)
        termo += razao
    print()
    adc = int(input('Quantas razões adicionais deseja ver? '))
system('clear')
fim = input('Voce deseja ver a Progresão completa que voce criou? [S / N] ').upper()
if fim == 'S':
    print(*pa)
elif fim == 'N':
    print('Beleza então')
else:
    print('Então some então')
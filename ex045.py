from time import sleep
from os import system
from random import randint

print('------ PEDRA PAPEL OU TESOURA ---------')
sleep(0.5)
print('[1] PEDRA')
print('[2] PAPEL')
print('[3] TESOURA')
pc = int(input('ESCOLHA UM DOS TRÊS - '))
cc = randint(1,3)
system('clear')

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(0.5)
system('clear')

#EMPATE
if pc == cc :
    if pc == 1:
        pc = ['PEDRA']
    elif pc == 2:
        pc = ['PAPEL']
    elif pc == 3:
        pc = ['TESOURA']
    if cc == 1:
        cc = ['PEDRA']
    elif cc == 2:
        cc = ['PAPEL']
    elif cc == 3:
        cc = ['TESOURA']
    print(f'VOCE ESCOLHEU {''.join(pc)}')
    print(f'O COMPUTADOR ESCOLHEU {''.join(cc)}')
    print('--------EMPATE---------')

#ESCOLHA DE PEDRA
elif pc == 1 and cc == 2:
    print(f'VOCE ESCOLHEU PEDRA')
    print(f'O COMPUTADOR ESCOLHEU PAPEL')
    print('--------DERROTA---------')
elif pc == 1 and cc == 3:
    print(f'VOCE ESCOLHEU PEDRA')
    print(f'O COMPUTADOR ESCOLHEU TESOURA')
    print('--------VITÓRIA---------')

#ESCOLHA DE PAPEL
if pc == 2 and cc == 1:
    print(f'VOCE ESCOLHEU PAPEL')
    print(f'O COMPUTADOR ESCOLHEU PEDRA')
    print('--------VITORIA---------')
elif pc == 2 and cc == 3:
    print(f'VOCE ESCOLHEU PAPEL')
    print(f'O COMPUTADOR ESCOLHEU TESOURA')
    print('--------DERROTA---------')

#ESCOLHA DE TESOURA
if pc == 3 and cc == 1:
    print(f'VOCE ESCOLHEU TESOURA')
    print(f'O COMPUTADOR ESCOLHEU PEDRA')
    print('--------DERROTA---------')
elif pc == 3 and cc == 2:
    print(f'VOCE ESCOLHEU TESOURA')
    print(f'O COMPUTADOR ESCOLHEU PAPEL')
    print('--------VITORIA---------')

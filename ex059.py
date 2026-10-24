from time import sleep
from os import system
escolha = 4
while escolha != 5:
    if escolha == 4:
        system('clear')
        n1 = int(input('Escolha um numero: '))
        n2 = int(input('Escolha outro numero: '))
        system('clear')
    sleep(3)
    print('-------- Escolha uma opção do menu a seguir --------')
    print('[1] SOMAR' \
    '\n[2] MULTIPLICAR' \
    '\n[3] MOSTRAR MAIOR NUMERO' \
    '\n[4] NOVOS NUMEROS' \
    '\n[5] SAIR DO PROGRAMA')
    escolha = int(input(''))
    if escolha == 1:
        system('clear')
        print(f'A soma de {n1} e {n2} é {(n1 + n2)}')
    elif escolha == 2:
        system('clear')
        print(f'A multiplicação de {n1} e {n2} é {(n1 * n2)}')
    elif escolha == 3:
        system('clear')
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior numero é {n1}')
        elif n2 > n1:
            print(f'Entre {n1} e {n2} o maior numero é {n2}')
        else:
            print('Os numeros são iguais')
    elif escolha == 5:
        system('clear')
        print('Finalizando...')
        sleep(2)
        system('clear')
    else:
        print('Opção inválida')



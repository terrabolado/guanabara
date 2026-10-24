from random import randint
rand = randint(0,10)
print('Pensei em um numero entre 1 e 10, será que voce consegue descobrir?')
escolha = 500
c = 1
while escolha != rand:
    escolha = int(input('Escolha um numero entre 1 e 10: '))
    if escolha > rand:
        print(f'O numero é menor que {escolha}, tente novamente')
        c += 1
    if escolha < rand:
        print(f'O numero é maior que {escolha}, tente novamento')
        c += 1
print(f'Parabens, em {c} tentativas voce conseguiu encontrar o numero {rand}')

num = int(input('Digite um numero Inteiro: '))
print('Escolha uma base de conversão')
print('[1] converter para Binário')
print('[2] converter para Octal')
print('[3] converter para Hexadecimal')
escolha = int(input(''))
if escolha == 1:
    print(f'O numero {num} em Binário é igual a {bin(num)[2:]}')
elif escolha == 2:
    print(f'O numero {num} em Octal é igual a {oct(num)[2:]}')
elif escolha == 3:
    print(f'O numero {num} em Hexadecimal é igual a {hex(num)[2:]}')
else:
    print('Escolha invalida')

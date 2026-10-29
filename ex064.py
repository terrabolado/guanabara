stop = 1
soma = 0
cont = 0
while stop != 999:
    stop = int(input('Digite um número - '))
    if stop != 999:
        soma += stop
        cont += 1
print(f'Voce digitou {cont} numeros e a soma deles foi {soma}')

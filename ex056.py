mul = 0
soma = 0
df = ['M', 'F']
qnt = int(input('Quantas pessoas serão cadastradas? '))
for x in range(1, qnt + 1):
    nome = input(f'Qual o nome da {x}° pessoa? ')
    idade = int(input(f'Qual a idade da {x}° pessoa? '))
    sexo = input(f'Qual o sexo da {x}° pessoa? [M / F] - ').upper()
    soma += idade
    if sexo == df[1] and idade < 20:
        mul += 1
    if sexo == df[0]:
        if x == 1:
            nomevelho = nome
            idadevelho = idade
        else:
            if idadevelho < idade:
                idadevelho = idade
                nomevelho = nome
media = soma / (qnt)
print(f'A média de idade do grupo é {media :.0f}')
print(f'{mul} mulheres tem menos de 20 anos')
print(f'O nome do homem mais velho é {nomevelho} e sua idade é {idadevelho} anos')

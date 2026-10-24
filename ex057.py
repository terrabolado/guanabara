'''sexo = 'Q'
while sexo != 'M' and sexo != 'F':
    sexo = input('Qual seu sexo? [M / F] - ').upper().strip()[0]
    if sexo != 'M' and sexo != 'F':
        print('Opção inválida, tente novamente')'''


sexo = input('Informe seu sexo: [M / F] ').strip().upper()[0]
while sexo not in 'MF':
    sexo = input('Opção inválida, informe seu sexo: [M / F] ').strip().upper()[0]
if sexo == 'M':
    sexo = 'MASCULINO'
if sexo == 'F':
    sexo = 'FEMININO'
print(f'Sexo {sexo} registrado com sucesso')

n1 = float(input('Insira sua primeira nota: '))
n2 = float(input('Insira sua segunda nota: '))
media = (n1 + n2) / 2
print(f'A média do aluno foi {media}')
if media >= 7.0:
    print('O aluno foi aprovado')
elif media < 5.0:
    print(f'O aluno foi reprovado')
elif media <= 6.9:
    print(f'O aluno está de recuperação')

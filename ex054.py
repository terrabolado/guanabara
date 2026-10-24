maior = 0
menor = 0
pes = int(input('Quantas pessoas voce quer listar? '))
for i in range(1, pes + 1):
    ano = int(input(f'Em que ano nasceu a {i}° pessoa? '))
    idade = 2026 - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'Das sete pessoas listadas, {menor} são menores de idade e {maior} são maiores de idade')
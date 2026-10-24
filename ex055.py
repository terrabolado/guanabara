pesos = []
pes = int(input('Quantas pessoas voce quer registrar? '))
for peso in range(1, pes + 1):
    p = float(input(f'Insira o peso da {peso}° pessoa: '))
    pesos.append(p)
print(f'O maior peso da lista foi {max(pesos)}kg')
print(f'O menor peso da lista foi {min(pesos)}kg')
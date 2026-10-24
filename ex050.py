s = 0
for i in range(0, 5):
    n = int(input('Digite um numero: '))
    if (n % 2 == 0):
        s += n
print(f'A soma dos numeros pares digitados é {s}')

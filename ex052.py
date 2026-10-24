n = int(input('Escolha um numero: '))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        t += 1
        print('\033[34m', end=' ')
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
if (t > 2):
    print('\nESSE NUMERO NÃO É PRIMO')
else:
    print('\nO NUMERO É PRIMO')
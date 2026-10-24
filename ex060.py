n = int(input('Escolha um numero para ver seu fatorial: '))
c = n
f = 1
print(f'{n}! = ', end='')
while c > 0:
    print(f'{c}', end=' ')
    print('X ' if c > 1 else '= ', end='')
    f *= c
    c -= 1
print(f'{f}', end=' ')

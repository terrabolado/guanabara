esc = int(input('Escolha um numero para ver seu fatorial: '))
c = esc
tot = 1
print(f'{esc}! = ', end=' ')
for m in range(esc, 0, -1):
    print(f'{c}', end=' ')
    print(f'X' if c > 1 else '=', end=' ')
    tot *= c
    c -=1
print(tot)

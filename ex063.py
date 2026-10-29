nmr = int(input('Quantos termos de fibonacci voce quer ver? '))
fib = 1
fibo = [0]
print('0', end=' ')
for i in range(1, nmr + 1):
    print(fib, end=' ')
    fibo.append(fib)
    fib = fibo[(len(fibo) - 2)] + fibo[(len(fibo) - 1)]

palin = str(input('Digite uma frase: ')).upper()
split = palin.split()
juncao = ''.join(split)
inv = ''
for letra in range(len(juncao) - 1, -1, -1):
    inv += juncao[letra]
print(inv)
print(juncao)
if inv == juncao:
    print('Temos um palindromo!!!')
else:
    print('Essa frase não é um palindromo!!!')

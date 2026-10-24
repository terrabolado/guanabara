nas = int(input('Insira o ano de nascimento do atleta: '))
idade = 2026 - nas
print(f'Um atleta nascido em {nas} possui {idade} anos')
if 9 < idade <= 14:
    print('O atleta está na categoria Infantil')
elif idade < 0:
    print('Se acalme, seu atleta ainda não nasceu...')
elif 14 < idade <= 19:
    print('O atleta está na categoria Junior')
elif 19 < idade <= 25:
    print('O atleta está na categoria Sênior')
elif idade > 25:
    print('O atleta está na categoria Master')
elif idade < 9:
    print('O atleta está na categoria Mirim')

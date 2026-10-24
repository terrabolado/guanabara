nas = int(input('Qual seu ano de nascimento? '))
idade = 2026 - nas

if idade > 18:
    print(f'Uma pessoa nascida em {nas} tem {idade} anos e seu ano de alistamento foi {nas + 18}')
elif idade < 0:
    print('Se acalme, essa pessoa ainda não nasceu.')
elif idade < 18:
    print(f'Uma pessoa nascida em {nas} tem {idade} anos e seu ano de alistamento será {nas + 18}')
elif idade == 18:
    print(f'Uma pessoa nascida em {nas} tem {idade} anos e deve se alistar imediatamente')

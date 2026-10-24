peso = float(input('Qual seu peso? '))
alt = float(input('Qual sua altura? '))
imc = peso / (alt**2)

if 10 < imc < 18.5:
    print(f'Seu imc é {imc:.1f}, voce esta abaixo do peso')
elif 18.5 <= imc < 25:
    print(f'Seu imc é {imc:.1f}, voce está no peso ideal')
elif 25 <= imc < 30:
    print(f'Seu imc é {imc:.1f}, voce está em sobrepeso')
elif 30 <= imc < 40:
    print(f'Seu imc é {imc:.1f}, voce está obeso')
elif 40 <= imc <= 80:
    print(f'Seu imc é {imc:.1f}, voce está em obesidade mórbida')
else:
    print(f'!!!!!!!SEU IMC É {imc:.1f} E VOCE PRECISA SE CUIDAR COM URGENCIA!!!!!!!!!')

seg1 = int(input('Primeiro segmento: '))
seg2 = int(input('Segundo segmento: '))
seg3 = int(input('Terceiro segmento: '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Segmentos validos para um triangulo')
    if seg1 == seg2 == seg3:
        print('Triangulo Equilatero')
    elif seg1 != seg2 != seg3 and seg1 != seg3:
        print('Triangulo Escaleno')
    else:
        print('Triangulo Isóceles')
else:
    print('Segmentos invalidos para formar um triangulo')

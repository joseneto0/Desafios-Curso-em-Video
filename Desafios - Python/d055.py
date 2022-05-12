maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input('Peso da {}° pessoa: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else: 
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso: {} kg'.format(maior))
print('O menor peso: {} kg'.format(menor))

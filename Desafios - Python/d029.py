km = int(input('Velocidade do carro: '))
print('LIMITE DE 80KM/H')
if km > 80:
    print('VOCÊ FOI MULTADO')
    limite = km - 80
    multa = limite * 7
    print(f'Você terá que pagar R$ {multa} de multa')
else:
    print(f'Devagar se vai ao longe!')

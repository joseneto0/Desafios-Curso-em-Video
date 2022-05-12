dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos KM foram rodados? '))
custo = dias * 60
gaso = km * 0.15
print(f'Você deverá pagar R$ {custo + gaso}')
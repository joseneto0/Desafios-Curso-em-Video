km = int(input('Qual a distância da sua viagem? '))
if km <= 200:
    print(f'Você vai pagar R$ {km * 0.5} para chegar ao seu destino')
else:
    print(f'Você vai pagar R$ {km * 0.45} para chegar ao seu destino')
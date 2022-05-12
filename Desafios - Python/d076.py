listagem = ('Lápis', 3, 'Borracha', 2.5, 'Caderno', 10, 'Estojo', 4.25, 'Bolsa', 100, 'Canetas', 4)
print('=' * 40)
print('           LISTAGEM DE PREÇOS')
print('=' * 40)
for i in range(0, len(listagem)):
  if i % 2 == 0:
    print(f'{listagem[i]:.<30}', end='')
  else:
    print(f'R${listagem[i]:>7.2f}')
print('=' * 40)
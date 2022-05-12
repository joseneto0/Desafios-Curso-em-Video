lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = maior = soma_coluna = 0
for linha in range(0,3):
  for coluna in range(0,3):
    lista[linha][coluna] = int(input(f'Digite o valor para [{linha}, {coluna}]: '))
print('==' * 20)
for linha in range(0,3):
  for coluna in range(0,3):
    print(f'[{lista[linha][coluna]:^7}]', end='')
    if lista[linha][coluna] % 2 == 0:
      soma_pares += lista[linha][coluna]
  print()
for linha in range(0,3):
  soma_coluna += lista[linha][2] 
print('==' * 20)
print(f'A soma dos pares deu igual a {soma_pares}')
print(f'A soma dos valores da terceira coluna deu igual a {soma_coluna}')
for coluna in range(0,3):
  if lista[1][coluna] == 0:
    maior = lista[1][coluna]
  elif lista[1][coluna] > maior:
    maior = lista[1][coluna]
print(f'O maior valor da segunda linha é {maior}')
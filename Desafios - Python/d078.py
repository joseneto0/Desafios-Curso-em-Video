numeros = []
for i in range(5):
  numeros.append(int(input(f'Digite um valor para a posição {i}: ')))
print('=' * 20)
print(f'Você digitou os valores {numeros}')
print(f'O maior valor digitado foi {max(numeros)} nas posições ', end='')
for cont, valor in enumerate(numeros):
  if valor == max(numeros):
    print(f'{cont}...', end='')
print()
print(f'O menor valor digitado foi {min(numeros)} nas posições ', end='')
for cont, valor in enumerate(numeros):
  if valor == min(numeros):
    print(f'{cont}...', end='')
print()
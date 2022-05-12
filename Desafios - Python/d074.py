from random import randint
print('Os valores sorteados foram: ', end='')
aleatorio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
for i in aleatorio:
  print(f'{i}', end=' ')
print(f'\nO menor valor sorteado foi o {min(aleatorio)}')
print(f'O menor valor sorteado foi o {max(aleatorio)}')
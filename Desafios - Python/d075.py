n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
numeros = (n1, n2, n3, n4)
print(f'Você digitou os números: {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
  print(f'O valor 3 apareceu na {numeros.index(3) + 1}° posição')
else:
  print('O valor 3 não foi digitado')
print(f'Os valores pares digitados: ', end='')
for i in numeros:
  if i % 2 == 0:
    print(i, end=' ')
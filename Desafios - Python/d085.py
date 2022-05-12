lista = [[],[]]
dados = 0
for i in range(1, 8):
  dados = int(input(f'Digite o {i}° valor: '))
  if dados % 2 == 0:
    lista[0].append(dados)
  else:
    lista[1].append(dados)
print('-=' * 30)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares são: {lista[0]}')
print(f'Os valores ímpares são: {lista[1]}')
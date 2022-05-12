lista = []
dados = []
maior = menor = 0
while True:
  dados.append(input('Digite seu nome: '))
  dados.append(int(input('Digite seu peso: ')))
  if len(lista) == 0:
    maior = menor = dados[1]
  else:
    if dados[1] > maior:
      maior = dados[1]
    elif dados[1] < menor:
      menor = dados[1]
  lista.append(dados[:])
  dados.clear()
  continuar = input('Quer continuar? [S/N] ').upper()
  if continuar in 'N':
    break
print('-=' * 30)
print(f'Você cadastrou {len(lista)} pessoas')
print(f'O maior peso foi de {maior} kg. Pessoa(s) com maior peso: ', end='')
for pessoa in lista:
  if pessoa[1] == maior:
    print(f'[{pessoa[0]}]', end='')
print()
print(f'O menor peso foi de {menor} kg. Pessoa(s) com menor peso: ', end='')
for pessoa in lista:
  if pessoa[1] == menor:
    print(f'[{pessoa[0]}]', end='')
print()
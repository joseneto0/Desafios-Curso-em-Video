valores = []
continuar = 'S'
while continuar != 'N':
  numeros = int(input('Digite um valor: '))
  if numeros not in valores:
    print('Valor adicionado!')
    valores.append(numeros)
  else:
    print('Valor repetido! Não será adicionado')
  continuar = input('Quer continuar? [S/N] ').upper()
print(f'A lista em ordem crescente é: {sorted(valores)}')
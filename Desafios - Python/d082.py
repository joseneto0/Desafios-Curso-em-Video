lista_completa = []
lista_pares = []
lista_impar = []
continuar = 'S'
while continuar != 'N':
  valores = int(input('Digite um número: '))
  lista_completa.append(valores)
  if valores % 2 == 0:
    lista_pares.append(valores)
  else:
    lista_impar.append(valores)
  continuar = input('Quer continuar? [S/N] ').upper()
  if continuar == 'N':
    break
print('-=' * 30)
print(f'A lista completa é {lista_completa}')
print(f'A lista de pares é {lista_pares}')
print(f'A lista com ímpares é {lista_impar}')
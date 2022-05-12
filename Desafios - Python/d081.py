lista = []
continuar = 'S'
qntd_digitados = 0
while continuar != 'N':
  numeros = int(input('Digite um valor: '))
  qntd_digitados += 1
  lista.append(numeros)
  continuar = input('Quer continuar? [S/N] ').upper()
print('-=' * 30)
print(f'Você digitou {qntd_digitados} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 not in lista:
  print('O valor 5 não foi encontrado')
else:
  print('O valor 5 faz parte da lista!')
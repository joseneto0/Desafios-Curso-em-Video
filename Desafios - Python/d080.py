lista = []
for i in range(5):
  valores = int(input('Digite um valor: '))
  if i == 0 or valores > lista[-1]:
    lista.append(valores)
  else:
    posicao = 0
    while posicao < len(lista):
      if valores <= lista[posicao]:
        lista.insert(posicao, valores)
        break
      posicao += 1
print(f'A lista em ordem crescente é: {lista}')
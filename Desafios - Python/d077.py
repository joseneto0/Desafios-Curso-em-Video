palavras = ('arroz', 'feijao', 'macarrao', 'carne', 'programar', 'lactose', 'leite', 'computador')
for i in palavras:
  print(f'\nNa palavra {i} temos ', end='')
  for vogais in i:
    if vogais.lower() in 'aeiou':
      print(vogais, end=' ')
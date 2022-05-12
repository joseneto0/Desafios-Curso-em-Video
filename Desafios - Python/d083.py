lista = []
expressao = input('Digite sua expressão: ')
for paren in expressao:
  if paren == '(':
    lista.append('(')
  elif paren == ')':
    if len(lista) > 0:
      lista.pop()
    else:
      lista.append(')')
      break
if len(lista) == 0:
  print('Sua expressão está correta!')
else:
  print('Sua expressão está errada!')
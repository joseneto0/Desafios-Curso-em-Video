palavra = input().lower()
if palavra == palavra[::-1]:
    print('A palavra {} é um palindromo!'.format(palavra))
else:
    print('A palavra {} não é um palindromo'.format(palavra))

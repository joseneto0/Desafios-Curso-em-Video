import random
print('=======Advinhe o número de 0 a 5=======')
num = int(input('Digite o número: '))
comp = random.choice(range(0,5))
print(f'Número escolhido pelo computador: {comp}')
if num == comp:
    print('Parabéns, você escolheu o mesmo número que o computador')
else:
    print('Que pena! Tente outra vez')


print('======TABUADA======')
num = int(input('Digite um número: '))
print('A tabuada do número {} é: '.format(num))
for c in range(1, 11):
    tabuada = num * c
    print('{} * {} = {}'.format(num, c, tabuada))
print('=='*10)
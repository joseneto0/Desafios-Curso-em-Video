print('-=' * 5, 'FATORIAL', '-=' * 5)
num = int(input('Digite o número: '))
cont = num
fatorial = 1
for i in range(num, 0, -1):
    print('{} '.format(cont), end='')
    if cont > 1:
        print('x ', end='')
    else:
        print('= ', end='')
    fatorial *= cont
    cont -= 1
print('{}'.format(fatorial))


print('-=' * 5, 'FATORIAL', '-=' * 5)
num = int(input('Digite o número: '))
cont = num
fatorial = 1
while cont > 0:
    print('{} '.format(cont), end='')
    if cont > 1:
        print('x ', end='')
    else:
        print('= ', end='')
    fatorial *= cont
    cont -= 1
print('{}'.format(fatorial))
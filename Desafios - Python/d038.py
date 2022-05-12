print('-=' * 20)
print('Comparador de Números')
print('-=' * 20)
num = int(input('Digite o 1° número: '))
num2 = int(input('Digite o 2° número: '))
if (num > num2):
    print('O número {} é maior que o {}'.format(num, num2))
elif (num < num2):
    print('O número {} é menor que o {}'.format(num, num2))
else:
    print('Os números são iguais')
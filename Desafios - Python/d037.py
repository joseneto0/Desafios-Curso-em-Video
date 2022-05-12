print('-=' * 15)
print('Conversor de Bases')
print('-=' * 15)
valor = int(input('Digite o número: '))
print('[1] - BINÁRIO\n[2] - OCTAL\n[3] - HEXADECIMAL')
conv = int(input('Para qual base você quer converter? '))
if (conv == 1):
    binario = format(valor, 'b')
    print('O número {} em binário é: {}'.format(valor, binario))
elif (conv == 2):
    octal = format(valor, 'o')
    print('O número {} em octal é: {}'.format(valor, octal))
else:
    hexa = format(valor, 'h')
    print('O número {} em hexadecimal é: {}'.format(valor, hexa))
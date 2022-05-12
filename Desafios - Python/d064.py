soma = 0
cont = 0
n = 0
while n != 999:
    n = int(input('Digite um número: (999 para parar) '))
    cont += 1
    soma += n
print('Você digitou {} números até o 999'.format(cont - 1))
print('A soma de todos os números deu: {}'.format(soma - 999))
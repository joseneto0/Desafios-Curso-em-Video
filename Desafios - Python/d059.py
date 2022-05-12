num_1 = int(input('Digite um número: '))
num_2 = int(input('Digite outro número: '))
opcao = 0
while opcao != 5:
    print('-=' * 20)
    print('''    [1] - SOMA
    [2] - MULTIPLICACAO
    [3] - MAIOR
    [4] - NOVOS NÚMEROS
    [5] - SAIR DO PROGRAMA''')
    opcao = int(input('Qual sua opcão? '))
    if opcao == 1:
        soma = num_1 + num_2
        print('{} + {} = {}'.format(num_1, num_2, soma))
    elif opcao == 2:
        mult = num_1 * num_2
        print('{} x {} = {}'.format(num_1, num_2, mult))
    elif opcao == 3:
        if num_1 > num_2:
            maior = num_1
        else:
            maior = num_2
        print('O maior é o {}'.format(maior))
    elif opcao == 4:
        num_1 = int(input('Digite um novo número: '))
        num_2 = int(input('Digite outro novo número: '))
print('FIM DO PROGRAMA!')

        

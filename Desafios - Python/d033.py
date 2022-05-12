##JEITO + FÁCIL (mas sem IF)
##numeros = input('Digite 3 números: ').split(' ')
##n1 = int(numeros[0])
##n2 = int(numeros[1])
##n3 = int(numeros[2])
##print(f'O maior número é o {max(n1, n2, n3)} e o menor é o {min(n1, n2, n3)}')


##JEITO COM IF
n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))
if n1 > n2 and n1 > n3:
    print(f'O maior número é o {n1}')
if n2 > n1 and n2 > n3:
    print(f'O maior número é o {n2}')
if n3 > n1 and n3 > n2:
    print(f'O maior número é o {n3}')
if n1 < n2 and n1 < n3:
    print(f'O menor número é o {n1}')
if n2 < n1 and n2 < n3:
    print(f'O menor número é o {n2}')
if n3 < n1 and n3 < n2:
    print(f'O mempr número é o {n3}')



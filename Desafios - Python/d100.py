from random import randint
from time import sleep
def sorteia(numeros):
    for i in range(5):
        numeros.append(randint(1,10))
    print(f'Sorteado 5 valores da lista:',end=' ')
    for val in numeros:
        print(f'{val}', end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')


def somaPar(numeros):#
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {numeros}, temos {soma}')


numeros = []
sorteia(numeros)
somaPar(numeros)
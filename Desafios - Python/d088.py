from random import randint
from time import sleep
lista = []
jogos = []
print('--' * 10)
print('    JOGO DA MEGA SENA     ')
print('--' * 10)
qntd_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
contador = 0
total = 1
while total <= qntd_jogos:
    contador = 0
    while True:
        numeros = randint(1, 60)
        if numeros not in lista:
            lista.append(numeros)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-=' * 5, 'SORTEANDO', '-=' * 5)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('==' * 5, 'PROGRAMA ENCERRADO', '==' * 5)
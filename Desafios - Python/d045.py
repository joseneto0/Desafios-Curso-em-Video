import random
from time import sleep
print('-=' * 20)
print('Pedra, Papel ou Tesoura')
print('-=' *20)
print('[1] PEDRA')
print('[2] PAPEL')
print('[3] TESOURA')
jogador = int(input('Qual sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
lista = ['Pedra', 'Papel', 'Tesoura']
pc = random.choice(lista)
print('==' * 20)
if jogador == 1 and pc == 'Pedra' or jogador == 2 and pc == 'Papel' or jogador == 3 and pc == 'Tesoura':
    print(f'Jogada do PC: {pc}')
    print('Aaaah, deu empate')
elif jogador == 1 and pc == 'Papel' or jogador == 2 and pc == 'Tesoura' or jogador == 3 and pc == 'Pedra':
    print(f'Jogada do PC: {pc}')
    print('Haa, você \033[1;31mPERDEU\033')
else:
    print(f'Jogada do PC: {pc}')
    print('Parabéns, você venceu!')
print('==' * 20)

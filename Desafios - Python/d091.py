from operator import itemgetter
from random import randint
from time import sleep
from turtle import clear

dado = {}
rank = {}
dado["jogador1"] = randint(1, 6)
dado["jogador2"] = randint(1, 6)
dado["jogador3"] = randint(1, 6)
dado["jogador4"] = randint(1, 6)
print('Valores sorteados: ')
sleep(1)
for k, v in dado.items():
    print(f'  O {k} tirou {v}')
    sleep(1)
print('Ranking dos jogadores: ')
rank = sorted(dado.items(), key=itemgetter(1), reverse=True)
for i, r in enumerate(rank):
    print(f'  {i+1}° lugar: {r[0]} com {r[1]}')
    sleep(1)
import random
print('=======Advinhe o número de 0 a 10=======')
num = int(input('Digite o número: '))
comp = random.choice(range(0,10))
contador_de_vezes = 1
while num != comp:
    num = int(input('Você errou! Escolha outro número: '))
    contador_de_vezes += 1
print(f'Número escolhido pelo computador: {comp}')
print(f'Você teve que palpitar {contador_de_vezes} vezes até acertar')

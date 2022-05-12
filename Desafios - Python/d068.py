import random
print('=-' * 10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 10)
soma = 0
contador = 0
while True:
    v = int(input('Diga um valor: '))
    p_i = input('Par ou Ímpar? [P/I] ').upper()
    computador = random.randint(0, 50)
    soma = v + computador
    print(f'Você jogou {v} e o computador {computador}. Total = {soma}')
    if p_i == 'P' and soma % 2 == 0:
        print('Você VENCEU!\nVamos jogar novamente...')
        print('=-' * 10)
        contador += 1
    elif p_i == 'P' and soma % 2 != 0:
        print('Você Perdeu!')
        print('=-' * 10)
        print(f'GAME OVER! Você venceu {contador} vezes')
        break
    if p_i == 'I' and soma % 2 != 0:
        print('Você VENCEU!\nVamos jogar novamente...')
        print('=-' * 10)
        contador += 1
    elif p_i == 'I' and soma % 2 == 0:
        print('Você Perdeu!')
        print('=-' * 10)
        print(f'GAME OVER! Você venceu {contador} vezes')
        break
from time import sleep
def contador(inicio, fim, passo):
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    if inicio < fim and passo > 0:
        for i in range(inicio, fim+1, passo):
            print(f'{i}' , end=' ', flush=True)
            sleep(0.5)
        print('FIM!')
    elif inicio > fim and passo > 0:
        for i in range(inicio, fim-1, -passo):
            print(f'{i}' , end=' ', flush=True)
            sleep(0.5)
        print('FIM!')
        print('-=' * 20)
    elif inicio > fim and passo < 0:
        for i in range(inicio, fim-1, passo):
            print(f'{i}' , end=' ', flush=True)
            sleep(0.5)
        print('FIM!')
        print('-=' * 20)


contador(1, 10, 1)
contador(10,0,2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
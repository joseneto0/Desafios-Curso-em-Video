from time import sleep
def maior(*numeros):
    if len(numeros) == 0:
        print('-=' * 30)
        print('Analisando os valores passados...')
        print('Foram informados 0 valores ao todo.')
        print('O maior valor informado foi 0')
    else:
        print('-=' * 30)
        print('Analisando os valores passados...')
        for i in numeros:
            print(f'{i}', end=' ', flush=True)
            sleep(0.5)
        print(f'Foram informados {len(numeros)} ao todo.')
        print(f'O maior valor informado foi {max(numeros)}')
    
    
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
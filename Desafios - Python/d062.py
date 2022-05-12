print('==' * 20)
print('PROGRESSÃO ARITMÉTICA')
print('==' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
novos = 10
while novos != 0:
    total += novos
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    novos = int(input('Você quer ver + quantos termos? '))
print('FIM')
print('O total de termos foi {}'.format(total))
    
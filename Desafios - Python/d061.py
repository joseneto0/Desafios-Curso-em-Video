print('==' * 20)
print('PROGRESSÃO ARITMÉTICA')
print('==' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM', end='')
    
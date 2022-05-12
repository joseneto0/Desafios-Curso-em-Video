print('==' * 20)
print('PROGRESSÃO ARITMÉTICA')
print('==' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
dec = primeiro + (11 - 1) * razao
for primeiro in range(primeiro , dec, razao):
    print('{}'.format(primeiro), end=' -> ')
print('FIM')
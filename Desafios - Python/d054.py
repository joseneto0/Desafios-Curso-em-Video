from datetime import date
contador_menor = 0
contador_maior = 0
ano_atual = date.today().year
for i in range(7):
    ano = int(input('Digite o ano da {}° pessoa: '.format(i + 1)))
    if ano_atual - ano >= 18:
        contador_maior += 1
    elif ano_atual - ano < 18:
        contador_menor +=1
print('No total {} pessoas são maiores de idade'.format(contador_maior))
print('E também {} pessoas são menores de idade'.format(contador_menor))
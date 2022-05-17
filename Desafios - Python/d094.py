lista = []
info = {}
soma = 0
while True:
    info.clear()
    info["nome"] = input('Nome: ')
    while True:
        info["sexo"] = input('Sexo: [M/F] ').upper()
        if info["sexo"] in 'MF':
            break
        else:
            print('Apenas M ou F')
    info["idade"] = int(input('Idade: '))
    soma += info['idade']
    lista.append(info.copy())
    while True:
        continuar = input('Quer continuar? [S/N] ')
        if continuar in 'SsNn':
            break
        else:
            print('Apenas S ou N')
    if continuar in 'Nn':
        break
print('-=' * 30)
print(f'- Foram cadastradas no total {len(lista)} pessoas')
media = soma / len(lista)
print(f'- A média de idade é de {media:.2f} anos.')
print('- As mulheres cadastradas foram ', end='')
for i in lista:
    if i['sexo'] == 'F':
        print(f'{i["nome"]}', end=' ')
print()
print('Lista das pessoas acima da média de idade: ')
print()
for c in lista:
    if c['idade'] > media:
        print(f'nome = {c["nome"]}; sexo = {c["sexo"]}; idade = {c["idade"]}')
        print()
print('<< FIM >> ')
print('-=' * 20)
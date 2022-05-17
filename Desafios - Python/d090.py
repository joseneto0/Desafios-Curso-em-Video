nome = {}
nome['nome'] = input('Digite seu nome: ')
nome['média'] = float(input('Digite sua média: '))
print(f'Nome é igual a {nome["nome"]}')
print(f'Média é igual a {nome["média"]}')
if nome['média'] < 7.0:
    nome['situação'] = 'Reprovado'
else:
    nome['situação'] = 'Aprovado'
print(f'Situação é igual a {nome["situação"]}')
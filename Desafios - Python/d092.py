dados = {}
dados["nome"] = input('Digite seu nome: ')
ano = int(input('Ano de Nascimento: '))
dados["idade"] = 2022 - ano
dados["cpts"] = int(input('Carteira de Trabalho [0 caso não tenha]: '))
if dados["cpts"] != 0:
    dados["contratação"] = int(input('Ano de Contratação: '))
    dados["salário"] = float(input('Salário: R$ '))
    dados["aposentadoria"] = dados['idade'] + ((dados['contratação'] + 35) - 2022)
print('-=' * 20)
for i, k in dados.items():
    print(f'{i} tem o valor {k}')
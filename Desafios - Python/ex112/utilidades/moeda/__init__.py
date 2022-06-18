def metade(preco=0):
    calc = preco / 2
    return moeda(calc)


def dobro(preco=0):
    calc = preco * 2
    return moeda(calc)


def aumentar(preco=0, taxa=0):
    calc = preco + (preco * taxa / 100)
    return moeda(calc)


def diminuir(preco=0, taxa=0):
    calc = preco - (preco * taxa / 100)
    return moeda(calc)



def moeda(preco=0):
    return f'R$ {preco:.2f}'.replace('.', ',')


def resumo(preco, aumento=10, reducao=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco)}')
    print(f'Metade do preço: \t{metade(preco)}')
    print(f'{aumento}% de aumento: \t{aumentar(preco, aumento)}')
    print(f'{reducao}% de redução: \t{diminuir(preco, reducao)}')
    print('-' * 30)
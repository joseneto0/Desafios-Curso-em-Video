def metade(preco=0):
    calc = preco / 2
    return calc


def dobro(preco=0):
    calc = preco * 2
    return calc


def aumentar(preco=0, taxa=0):
    calc = preco + (preco * taxa / 100)
    return calc


def diminuir(preco=0, taxa=0):
    calc = preco - (preco * taxa / 100)
    return calc


def moeda(preco=0):
    return f'R$ {preco:.2f}'.replace('.', ',')
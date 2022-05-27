def metade(preco=0, formatado=False):
    calc = preco / 2
    if formatado == True:
        return moeda(calc)
    else:
        return calc


def dobro(preco=0, formatado=False):
    calc = preco * 2
    if formatado == True:
        return moeda(calc)
    else:
        return calc


def aumentar(preco=0, taxa=0, formatado=False):
    calc = preco + (preco * taxa / 100)
    if formatado == True:
        return moeda(calc)
    else:
        return calc


def diminuir(preco=0, taxa=0, formatado=False):
    calc = preco - (preco * taxa / 100)
    if formatado == True:
        return moeda(calc)
    else:
        return calc


def moeda(preco=0):
    return f'R$ {preco:.2f}'.replace('.', ',')


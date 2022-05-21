def fatorial(num, show=False):
    """
    Calculo o Fatorial de um número:
    :param num: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: Retorna o fatorial do valor num
    """
    print('=' * 25)
    if show == False:
        fato = 1
        for i in range(num, 0, -1):
            fato *= i
        return fato
    else:
        fato = 1
        for i in range(num, 0, -1):
            if i > 1:
                print(f'{i} x', end=' ')
            else:
                print(f'{i}', end=' ')
            fato *= i
        return f'= {fato}'


#programa principal:
print(fatorial(5, True))
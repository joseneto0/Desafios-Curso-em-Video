def linha():
    print('-=' * 26)


def leiaInt(numero):
    """
    Ler um valor e falar se é númerico ou não
    :param numero: valor digitado pelo usuário
    :param return: retorna uma mensagem em verde, caso o valor seja númerico,
    """
    linha()
    while numero.isnumeric() == False:
        print('\033[1;31mERRO! Você não digitou um número')
        linha()
        numero = input('Digite um número: ')
    linha()
    return f'\033[1;32mVocê digitou o número: {numero}'
    

#programa principal
n = input('Digite um número: ')
print(leiaInt(n))
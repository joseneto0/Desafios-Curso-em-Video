from time import sleep
def escreva(msg):
    """
    Deixa os traçados ao redor da palavra
    """
    l = len(msg) + 2
    print('~' * l)
    print(f' {msg}')
    print('~' * l)


def manual(comando):
    """
    Acessa o help do comando digitado pelo usuario
    """
    escreva(f" \033[1;104mAcessando o manual do comando '{comando}'")
    sleep(1)
    print(help(comando)) 
    

#programa principal
while True:
    escreva(f'\033[1;102mSISTEMA DE AJUDA PyHELP')
    com = input('Função ou Biblioteca . ') 
    if com == 'FIM':
        break
    manual(com)
    print('-=' * 20)

#fico bem feinho, mas ta funfando :3
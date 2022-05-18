def escreva(msg):
    l = len(msg) + 2
    print('~' * l)
    print(f' {msg}')
    print('~' * l)
    
while True: 
    palavra = input('Digite sua palavra: [n para parar] ')
    if palavra in 'n':
        break
    escreva(palavra)
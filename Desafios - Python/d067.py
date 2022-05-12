while True:
    print('---' * 10)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('---' * 10)
    if n > 0:
        for i in range(1, 11):
            print(f'{n} x {i} = {n*i}')
    else:
        break
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
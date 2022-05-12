print('-=' * 20)
print('Sequência de Fibonacci')
print('-=' * 20)
n = int(input('Quantos números da sequência você quer ver? '))
F1 = 1
F2 = 1
print('{} -> {}'.format(F1, F2), end='')
cont = 3
while cont <= n:
    seq = F1 + F2
    print(' -> {}'.format(seq), end='')
    F1 = F2
    F2 = seq
    cont +=1
print(' FIM')
num = int(input('Número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        total += 1
if total == 2:
    print('o número é primo')
else:
    print('o número não é primo')
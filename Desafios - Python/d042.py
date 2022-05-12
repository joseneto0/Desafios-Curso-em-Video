print('-=' * 20)
print('Analisador de triângulos')
print('-=' * 20)
a = float(input('Primeiro comprimento: '))
b = float(input('Segundo comprimento: '))
c = float(input('Terceiro comprimento: '))
if a + b > c and a + c > b and b + c > a:
    print('É possível formar um triângulo')
    if a == b == c:
        print('Seu triângulo é Equilátero!')
    elif a == b != c or a == c != b or b == c != a:
        print('Seu triângulo é Isósceles!')
    else:
        print('Seu triângulo é Escaleno')
else:
    print('Não é possível formar um triângulo')


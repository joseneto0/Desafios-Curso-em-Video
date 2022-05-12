print('-=' * 20)
print('Analisador de triângulos')
print('-=' * 20)
a = float(input('Primeiro comprimento: '))
b = float(input('Segundo comprimento: '))
c = float(input('Terceiro comprimento: '))
if a + b > c and a + c > b and b + c > a:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')


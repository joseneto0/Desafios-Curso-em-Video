numeros = 0
media = 0
cont = 0
soma = 0
maior = 0
menor = 0
while numeros >= 0:
    numeros = int(input('Digite um número: '))
    cont += 1
    soma += numeros
    if cont == 1:
        maior = menor = numeros
    elif numeros > maior:
        maior = numeros
    elif numeros < menor:
        menor = numeros
    continuar = input('Quer continuar? [s/n] ').lower()
    if continuar == 'n':
        break
media = soma / cont
print('Você digitou {} números e a média dos valores deu: {:.2f}'.format(cont, media))
print('O maior valor é o {} e o menor é o {}'.format(maior, menor))
print('Fim do Programa')

contador_feminino = 0
soma = 0
maior_idade = 0
nome_velho = ''
for i in range(1, 5):
    print('----- {}° PESSOA -----'.format(i))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper().strip()
    soma += idade
    media = soma / 4
    if sexo == 'F' and idade < 20:
        contador_feminino += 1
    if sexo == 'M' and i == 1:
        if idade > maior_idade:
            maior_idade = idade
            nome_velho = nome
        elif maior_idade > idade:
            nome_velho = nome
            maior_idade = idade
    if sexo == 'M' and idade > maior_idade:
        nome_velho = nome
        maior_idade = idade
print('A média de idade do grupo é de {:.1f} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maior_idade, nome_velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(contador_feminino))
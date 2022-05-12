print('-----' * 10)
print('LOJA DO ZEZIN')
print('-----' * 10)
soma = 0
produtos_1000 = 0
produto_barato = 0
nome_produto_barato = ''
contador = 0
while True:
    nome = input('Nome do Produto: ')
    preço = float(input('Preço: R$ '))
    contador += 1
    soma += preço
    if contador == 1 or preço < produto_barato:
        produto_barato = preço
        nome_produto_barato = nome
    else:
        if preço < produto_barato:
            produto_barato = preço
            nome_produto_barato = nome
    if preço > 1000:
        produtos_1000 += 1
    continuar = input('Quer continuar? [S/N] ').upper()
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').upper()
    if continuar == 'N':
        print('------ FIM DO PROGRAMA ------')
        print(f'O total da compra foi {soma:.2f}')
        print(f'Temos {produtos_1000} produtos custando mais de R$1000.00')
        print(f'O produto mais barato foi {nome_produto_barato} que custou R${produto_barato}')
        break
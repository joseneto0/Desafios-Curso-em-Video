homens_cadastrados = 0
mulheres_20 = 0
pessoas_18 = 0
while True:
    print('---' * 10)
    print('CADASTRE UMA PESSOA')
    print('---' * 10)
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ').upper()
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').upper()
    if idade > 18:
        pessoas_18 += 1
    if sexo == 'M':
        homens_cadastrados += 1
    if sexo == 'F' and idade < 20:
        mulheres_20 += 1
    continuar = input('Quer continuar? [S/N] ').upper()
    if continuar == 'N':
        break
    while continuar not in 'S':
        continuar = input('Quer continuar? [S/N] ').upper()
print('====== FIM DO PROGRAMA ======')
print(f'Total de pessoas com mais de 18 anos: {pessoas_18}')
print(f'Ao todo, temos {homens_cadastrados} homens cadastrados')
print(f'E temos {mulheres_20} mulheres com menos de 20 anos')
    
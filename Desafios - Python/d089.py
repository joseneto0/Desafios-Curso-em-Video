lista = []
while True:
    nome = input('Digite seu nome: ')
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2
    lista.append([nome, [nota_1, nota_2], media])
    continuar = input('Quer continuar? [S/N] ')
    if continuar in 'Nn':
        break
print('==' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opcao = int(input('Você quer ver a nota de qual aluno? [999 interrompe] '))
    if opcao == 999:
        break
    if opcao <= len(lista) - 1:
        print(f'Notas de {lista[opcao][0]} são {lista[opcao][1]}')
print("CABO :3")
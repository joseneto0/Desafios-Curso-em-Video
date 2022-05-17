dados = {}
lista = []
gols = []
while True:
    print('-' * 20)
    dados.clear()
    dados["nome"] = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    gols.clear()
    for p in range(partidas):
        gols.append(int(input(f'Quantos gols na partida {p}? ')))
    dados["gols"] = gols[:]
    dados["total"] = sum(gols)
    lista.append(dados.copy())
    continuar = input('Quer continuar? [S/N] ').upper()
    if continuar in 'N':
        break
print('-=' * 30)
print(f'{"cod nome":20} {"gols":20} {"total":<20}')
print('--' * 24)
for i, v in enumerate(lista):
    print(f'{i:>4}' ,end='')
    for d in v.values():
        print(f'{str(d):<20}' ,end='')
    print()
print('--' * 24)

while True:
    mostrar = int(input('Mostrar dados de qual jogador? [999 para encerrar] '))
    if mostrar == 999:
        break
    if mostrar >= len(lista):
        print('ERRO')
    else:
        print(f'---- LEVANTAMENTO DO JOGADOR {lista[mostrar]["nome"]}')
        for i, g in enumerate(lista[mostrar]["gols"]):
            print(f'   No jogo {i+1} fez {g} gols')
    print('--' * 24)
print('FIM')
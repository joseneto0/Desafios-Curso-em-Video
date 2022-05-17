from time import sleep
dados = {}
gols = []
dados["nome"] = input('Nome do Jogador: ')
dados["partidas"] = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for i in range(dados['partidas']):
    dados["gols"] = gols
    qntd_gols = int(input(f'Quantos gols na partida {i+1}? '))
    gols.append(qntd_gols)
dados["soma"] = sum(gols)
print('-=' * 20)
for c, k in dados.items():
    print(f'O campo {c} tem o valor {k}')
print('-=' * 20)
print(f'O jogador {dados["nome"]} jogou {dados["partidas"]} partidas')
for p, g in enumerate(gols):
    print(f'   => Na partida {p+1}, fez {g} gols')
    sleep(1)
print(f'Foi um total de {sum(gols)} gols')
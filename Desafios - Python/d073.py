times = ('Corithians', 'Bragantino', 'Atlético-MG', 'Coritiba', 'São Paulo', 'Santos', 'Cuiabá', 'Internacional', 'Avaí', 'América-MG', 'Palmeiras', 'Flamengo', 'Botafogo', 'Fluminense', 'Ceará', 'Athletico-PR', 'Atlético-GO', 'Goiás', 'Juventude', 'Fortaleza')
print(f'Os times do brasileirão são: {times}')
print('==' * 25)
print(f'Os cinco primeiros times do brasileirão são: {times[:5]}')
print('==' * 25)
print(f'Os cinco últimos da tabela são: {times[15:]}')
print('==' * 25)
print(f'Os times em ordem alfabética: {sorted(times)}')
print('==' * 25)
print(f'O Palmeiras está na posição: {times.index("Palmeiras")+1}°')
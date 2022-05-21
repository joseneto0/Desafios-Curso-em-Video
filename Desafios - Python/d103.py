def ficha(nome='<desconhecido>', gols=0):
    '''
    Mostra o nome e os gols marcados mesmo sem nada digitado
    :param nome: Nome do jogador
    :param gols: Quantidade de gols do jogador
    :return: retorna a string completa
    '''
    print('-=' * 25)
    return f'O jogador {nome} fez {gols} gol(s) no campeonato'


#programa principal
num = input('Digite o nome do jogador: ')
gol = input('Total de gols: ')
if gol.isnumeric():
    g = int(gol)
else:
    gol = 0
if num.strip() == '':
    print(ficha(gols=gol)) 
else:
    print(ficha(num, gol)) 
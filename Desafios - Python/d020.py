import random
print('======== 4 ALUNOS ==========')
primeiro = str(input('1° Aluno: '))
segundo = str(input('2° Aluno: '))
terceiro = str(input('3° Aluno: '))
quarto = str(input('4° Aluno: '))
nomes = [primeiro, segundo, terceiro, quarto]
random.shuffle(nomes)
print(f'Ordem de apresentação: {nomes}')

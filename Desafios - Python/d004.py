algo = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(algo)}')
print(f'Tem espaços? {algo.isspace()}')
print(f'É um número? {algo.isnumeric()}')
print(f'É alfabético? {algo.isalpha()}')
print(f'É alfanumérico? {algo.isalnum()}')
print(f'Está em maiúsculo? {algo.isupper()}')
print(f'Está em minúsculo? {algo.islower()}')
print(f'Está capitalizada? {algo.istitle()}')
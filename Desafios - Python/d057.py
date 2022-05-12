sexo = input('Digite seu sexo [M/F]: ').upper().strip()
while sexo not in 'MF':
    sexo = input('Digite novamente [M/F]: ').upper().strip()
print('Sexo {}'.format(sexo))

    

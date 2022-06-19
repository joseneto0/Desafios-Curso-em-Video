def leiaInt():
    while True:
        try:
            num = int(input('Digite um número inteiro: '))
        except KeyboardInterrupt:
            print('\033[1;31mERRO! O usuário decidiu não digitar o número\033[m')
            return 0
        except:
            print('\033[1;31mERRO! Você não digitou um número inteiro\033[m')
            continue
        else:
            return num



def leiaFloat():
    while True:
        try:
            num = float(input('Digite um número real: '))
        except KeyboardInterrupt:
            print('\033[1;31mERRO! O usuário decidiu não digitar o número\033[m')
            return 0
        except:
            print('\033[1;31mERRO! Você não digitou um número real\033[m')
            continue
        else:
            return num


# prog principal
numero_inteiro = leiaInt()
numero_real = leiaFloat()
print(f'O valor inteiro digitado foi {numero_inteiro} e o real foi o {numero_real}')

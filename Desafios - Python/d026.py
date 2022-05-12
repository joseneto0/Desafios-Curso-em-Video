frase = str(input('Digite uma frase: ')).strip()
print(f'A frase tem {frase.upper().count("A")} letras A')
print(f'O primeiro A está na casa {frase.find("a")+1}')
print(f'O ultimo A está na casa {frase.rfind("a")+1}')



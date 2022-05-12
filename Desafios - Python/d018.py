import math
ang = float(input('Digite o valor do ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print(f'O ângulo {ang}° tem como seno: {sen:.2f}')
print(f'O ângulo {ang}° tem como cosseno: {cos:.2f}')
print(f'O ângulo {ang}° tem como tangente: {tang:.2f}')



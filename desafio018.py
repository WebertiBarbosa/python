from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))

print(f'O ângulo {ang} tem o seno {sen:.2f}, cosseno {cos:.2f} e a tangente {tan:.2f}.')

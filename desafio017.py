import math
catOposto = float(input('Digite o valor do cateto oposto do triângulo: '))
catAdjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.hypot(catOposto, catAdjacente)

print(f'O valor da hipotenusa é {hipotenusa}')


km = float(input('Digite a quantidade de quilômetros rodados pelo carro: '))
dias = int(input('Digite a quantidade de dias de locação: '))
preco_por_km = 0.15
preco_por_dia = 60
valor_dia_total = dias * preco_por_dia
valor_km_total = km * preco_por_km
valor_total = valor_dia_total + valor_km_total
print(f'O valor referente a {km:.2f}Km percorridos é R${valor_km_total:.2f}.')
print(f'O valor referente a locação do veículo por {dias} dias é R${valor_dia_total:.2f}.')
print(f'O valor total a pagar é R${valor_total:.2f}.')

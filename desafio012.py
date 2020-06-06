preco = float(input('Digite o valor do produto: R$ '))
desconto = 5 / 100
valor_descontado = preco * desconto
valor_novo = preco - (preco * desconto)
print(f'O valor original do produto é R${preco:.2f}')
print(f'O valor descontado é R${valor_descontado:.2f}')
print(f'O valor com desconto de {desconto*100:.2f}% é de R${valor_novo:.2f}')

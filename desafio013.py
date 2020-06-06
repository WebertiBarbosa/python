sal = float(input('Digite o salário atual: R$'))
print(f'O salário atual é de R${sal:.2f}')
aumento = 15 / 100
valor_aumento = sal * aumento
print(f'O aumento de {aumento*100:.2f}% equivale a R${valor_aumento:.2f}')
sal_novo = sal + valor_aumento
print(f'Parabéns! Seu novo salário é R${sal_novo:.2f}')
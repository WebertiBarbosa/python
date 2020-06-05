sal = float(input('Digite o salário atual: R$'))
print(f'O salário atual é R${sal:.2f}')
aumento = 0.15
valor_aumento = sal * aumento
print(f'O valor do aumento de {aumento*100:.2f}% é R${valor_aumento:.2f}')
sal_novo = sal + valor_aumento
print(f'Parabéns! Esse é seu novo salário: R${sal_novo:.2f}')
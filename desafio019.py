from random import choice
aluno1 = str(input('Digite o nome do aluno: '))
aluno2 = str(input('Digite o nome de um novo aluno: '))
aluno3 = str(input('Digite o nome de um novo aluno: '))
aluno4 = str(input('Digite o nome de um novo aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]

print('O aluno escolhido foi:', choice(lista))






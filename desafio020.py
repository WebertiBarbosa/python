from random import shuffle
aluno1 = str(input('Digite o nome do aluno: '))
aluno2 = str(input('Digite outro nome: '))
aluno3 = str(input('Digite outro nome: '))
aluno4 = str(input('Digite outro nome: '))

lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)

print(lista)



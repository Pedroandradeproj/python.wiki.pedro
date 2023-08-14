# Faça um programa que calcule o número médio de alunos por turma. 
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
# As turmas não podem ter mais de 40 alunos.

qtdturma=int(input("Informe a quantidade de turmas : "))

qalunos=0


for i in range (qtdturma):
    alunos=int(input("Informe a quantidade de alunos na turma : "))
    while alunos>40 or alunos<0 :
        alunos=int(input(" As turmas não podem ter mais de 40 alunos. Digite Novamente : "))
    qalunos+=alunos    
 
mediaalu=qalunos/qtdturma
print(f"o número médio de alunos por turma : {mediaalu}")
# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.

media=[]
aluno=1
seguencia = ["primeira", "segunda", "terceira" ,"quarta"]
for i in range (10):
    print(f"Aluno {aluno}")
    nota=0
    for i in range(4):
        nota+=float(input(f"Digite a {seguencia[i]} nota do aluno {aluno} : "))       
    media1= nota/4
    if media1 >= 7:
        media.append(f"Aluno {aluno} = {media1}")
    aluno+=1
    
print(media)

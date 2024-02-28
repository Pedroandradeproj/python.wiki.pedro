#Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com
# mais de 13 anos possuem altura inferior à média de altura desses alunos.

vetor = [
    {"aluno": 1, "idade": 18, "altura": 1.63},
    {"aluno": 2, "idade": 27, "altura": 1.83},
    {"aluno": 3, "idade": 60, "altura": 1.75},
    {"aluno": 4, "idade": 22, "altura": 1.70},
    {"aluno": 5, "idade": 19, "altura": 1.68},
    {"aluno": 6, "idade": 25, "altura": 1.79},
    {"aluno": 7, "idade": 13, "altura": 1.71},
    {"aluno": 8, "idade": 21, "altura": 1.76},
    {"aluno": 9, "idade": 20, "altura": 1.82},
    {"aluno": 10, "idade": 24, "altura": 1.74},
    {"aluno": 11, "idade": 19, "altura": 1.65},
    {"aluno": 12, "idade": 26, "altura": 1.78},
    {"aluno": 13, "idade": 8, "altura": 1.85},
    {"aluno": 14, "idade": 20, "altura": 1.73},
    {"aluno": 15, "idade": 32, "altura": 1.69},
    {"aluno": 16, "idade": 21, "altura": 1.77},
    {"aluno": 17, "idade": 23, "altura": 1.81},
    {"aluno": 18, "idade": 9, "altura": 1.67},
    {"aluno": 19, "idade": 25, "altura": 1.76},
    {"aluno": 20, "idade": 27, "altura": 1.84},
    {"aluno": 21, "idade": 20, "altura": 1.70},
    {"aluno": 22, "idade": 12, "altura": 1.68},
    {"aluno": 23, "idade": 46, "altura": 1.79},
    {"aluno": 24, "idade": 29, "altura": 1.87},
    {"aluno": 25, "idade": 18, "altura": 1.72},
    {"aluno": 26, "idade": 24, "altura": 1.75},
    {"aluno": 27, "idade": 21, "altura": 1.71},
    {"aluno": 28, "idade": 50, "altura": 1.80},
    {"aluno": 29, "idade": 23, "altura": 1.76},
    {"aluno": 30, "idade": 22, "altura": 1.68}
]

media=0
for i in range(30):
    media+=vetor[i]["altura"]
media/=30
alun = []
for i in range(30):
    if vetor[i]["idade"] >= 13:
        if vetor[i]["altura"] <= media :
            alun.append(vetor[i])
            
print(f"media : {media}")
print("alunos com mais de 13 anos com altura inferior à média de altura desses alunos" )
for i in range(len(alun)):
    print(alun[i])

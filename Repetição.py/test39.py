# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando
# o número do aluno e o segundo representando a sua altura em centímetros. Encontre
# o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número 
# do aluno mais baixo, junto com suas alturas.
nconj=4
alb=[]
alua=[]
maior=[]
menor=[]
for i in range(nconj):
    nal=int(input("Informe o número do aluno : "))
    altc=float(input("Informe altura do aluno : "))
    test=(f"Aluno {nal}  altura: {altc}")
    maior.append(test)
    menor.append(test)
    alb.append(altc)
    alua.append(altc)
    if alb[0]>altc:
        alb[0]=altc
        menor[0]=test
    if alua[0]<altc:
        alua[0]=altc
        maior[0]=test 
print(f"aluno mais alto  = {maior[0]}")        
print(f"aluno mais baixo = {menor[0]}")           
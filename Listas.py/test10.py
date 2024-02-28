#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
# cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
vetor1=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
vetor2=[5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
vetor3=[]
for i in range(10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])
    
print(vetor3)
#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

vetor1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
vetor2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
vetor3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])
    vetor3.append(vetor3[i])
    
print(vetor3)
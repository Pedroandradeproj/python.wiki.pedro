#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
vetor = []
soma=0
multi=1
for i in range(5):
    num=int(input("Digite numero inteiro: "))
    vetor.append(num)
    soma+=num
    multi*=num
    
print(f"soma = {soma}")
print(f"multiplicação = {multi}")
print(f"números : {vetor}") 
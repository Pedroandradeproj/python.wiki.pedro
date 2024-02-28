#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
vetor=[]
for i in range(10):
    num=int(input("informe Numero inteiro : "))
    soma= num*num
    vetor.append(soma)
for i in range(10):
    print(vetor[i])
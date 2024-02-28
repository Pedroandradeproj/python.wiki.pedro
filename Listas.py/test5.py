#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
# Imprima os três vetores


vetor=[]
vetorPar=[]
vetorImpares=[]
print("Digite 20 numeros inteiros ")
for i in range (20):
    num= int(input(f"{i+1}= Digite numero inteiro : "))
    if num%2 == 0 :
        vetorPar.append(num)
    else: vetorImpares.append(num)

print(f"vetor original : {vetor}")
print(f"vetor impares : {vetorImpares}")
print(f"vetor par : {vetorPar}")
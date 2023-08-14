# Faça um programa que, dado um conjunto de N números, 
# determine o menor valor, o maior valor e a soma dos valores.

qn=int(input("Informe quatidade de numero desejados : "))

n=int(input("Informe quatidade de numero desejados : "))

num=int(input("informe numero :" ))

soma=num
maior=num
menor=num
qn-=1

for i in range (qn):
    num=int(input("informe numero :" )) 
    if maior<num:
        maior=num              
    if menor>num:
        menor=num         
    soma+=num
    
print(f"soma dos valores : ",soma)
print(f"o maior valor : ",maior)
print(f"menor valor : ",menor)
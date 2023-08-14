# Faça um programa que leia uma quantidade indeterminada de números positivos e conte
# quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. 
# A entrada de dados deverá terminar quando for lido um número negativo.
q=1
lis1=0
lis2=0
lis3=0
lis4=0
l1=[]
l2=[]
l3=[]
l4=[]
while q>0:
    num=int(input("Informe número de 0 a 100: "))
    while num>100:
        num=int(input("tem que ser de 0 a 100: "))
    if num<0:
        q-=1
    elif num>=0 and num<=25 :
        lis1+=1
        l1.append(num)
    elif num>=26 and num<=50 :
        lis2+=1
        l2.append(num)    
    elif num>=51 and num<=75 :
        lis3+=1
        l3.append(num)
    elif num>=76 and num<=100 :
        lis4+=1
        l4.append(num)    
print(f"intervalos: [0-25]   = {lis1} = {l1}") 
print(f"intervalos: [26-50]  = {lis2} = {l2}")
print(f"intervalos: [51-75]  = {lis3} = {l3}")
print(f"intervalos: [76-100] = {lis4} = {l4}")       
        
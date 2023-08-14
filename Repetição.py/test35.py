# Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma
# lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário
num=int(input("Informe número inteiro : "))
n1=num
cal1=[]
cal=0

listareversa=[]
for i in range (num):
    con=num%n1
    if con==0:
        cal+=1
        cal1.append(n1)
    n1-=1    
if cal==2:
    print("O número e primo")
elif cal>2:
    print("O número  não e primo")

n=cal-1
    
for i in range (cal):
       listareversa.append(cal1[n])
       n-=1    

print(f"Lista de numeros que ele e dividido :",listareversa)

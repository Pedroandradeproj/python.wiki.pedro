# Altere o programa de cálculo dos números primos, informando, caso 
# o número não seja primo, por quais número ele é divisível.

num=int(input("Informe número inteiro : "))
n1=num
cal1=[]
cal=0
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

    
    
print(f"Lista de numeros que ele e dividido :",cal1)
print(f"Quandidade de numeros que ele e dividido :",cal)

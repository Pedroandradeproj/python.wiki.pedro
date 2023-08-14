# Os números primos possuem várias aplicações dentro da Computação, por exemplo na 
# Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo.
# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
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

# print(f"Lista de numeros que ele e dividido :",cal1)
# print(f"Quandidade de numeros que ele e dividido :",cal)

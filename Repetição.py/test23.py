# Faça um programa que mostre todos os primos entre 1 e N sendo N um número
# inteiro fornecido pelo usuário. O programa deverá mostrar também o número 
# de divisões que ele executou para encontrar os números primos. Serão avaliados
# o funcionamento, o estilo e o número de testes (divisões) executados.

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





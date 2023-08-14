# Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
print("Informe Numero Inteiro Positivo")
list=[]
conta=("")
num=input()
cont=(len(num))
numcont=cont-1

for i in range (cont):
    print(num[numcont])
    conta+=(num[numcont])
    list.append(num[numcont])
    
    numcont-=1

print(conta)
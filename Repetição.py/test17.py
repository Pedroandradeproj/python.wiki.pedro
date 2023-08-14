# Faça um programa que calcule o fatorial de um número
# inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
fat=int(input("Informe número fatorial : "))
cont=fat-1
contm=[fat]
mul=fat
res=fat
n=0
for i in range (cont):
    mul-=1
    contm[0]=(f"{contm[0]}.{mul}")
    res*=mul

print(f"{fat}!={contm[0]}={res}")
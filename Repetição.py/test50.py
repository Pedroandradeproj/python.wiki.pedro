# Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, 
# Faça um programa que calcule o valor de H com N termos
num=int(input("Informe o numero de N : "))
m=int(1)
n=int(1)
h=str(f"H = 1 + {n}/{m}")
res=float(0)
res+=1+n/m
num-=1
for i in range (num):
    m+=1
    h+=(f" + {n}/{m}")
    res+=n/m
h+=(".")
print(h)
print(f"Resultado= {res:.2f}")
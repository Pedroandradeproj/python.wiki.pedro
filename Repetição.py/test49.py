# Faça um programa que mostre os n termos da Série a seguir:
#  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 


num=int(input("Informe o numero de n desejados : "))
m=int(1)
n=int(1)
S=str(f"S = {n}/{m}")
res=float(0)
res+=n/m
num-=1
for i in range (num):
    n+=1
    m+=2
    S+=(f" + {n}/{m}")
    res+=n/m
S+=(".")
print(S)
print(f"Resultado= {res:.2f}")
# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e
# a quantidade de números impares
dez=10
par=[]
impar=[]
qpar=0
qimpar=0

for i in range (dez):
    num=int(input("Informe número inteiro : "))
    if num%2==0 :
        par.append(num)
        qpar+=1
    elif num%2==1 :
        impar.append(num)
        qimpar+=1
print(f"números pares :",par)
print(f"números impares :",impar)        

print(f"Quantidade números pares :",qpar)
print(f"Quantidade números impares :",qimpar)        

# unico jeito de fazer lista receber o numero e usando  .append()
# !!! nao usar .append= nao da certo 
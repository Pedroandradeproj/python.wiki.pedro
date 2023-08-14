# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro 
# número elevado ao segundo número. Não utilize a função de potência da linguagem.


base = int(input("Digite a base: "))
expoente = int(input("Digite expoente: "))
res=base
expoente-=1
for i in range(expoente):
    res*=base
    
print(res)
# * e operador e nao tem como multiplicar ele na frente nem atras do numero

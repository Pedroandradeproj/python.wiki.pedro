# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.
print("Informe primeiro número : ")
n1=float(input())
print("Informe segundo número :")
n2=float(input())
print("Informe qual operação deseja realizar :")
op=input()
print(f"{int(n1)}{op}{int(n2)}")
r1=n1+n2
r2=n1-n2
r3=n1*n2
r4=n1/n2
if op=="+" :
    print("resultado =",r1)
    if (r1%2)==1:print("Número impar")
    elif (r1%2)==0:print("Número par") 
    if r1>=0:print("valor e positivo")
    elif r1<0:print("valor e negativo") 
    if r1%1==0:print("Numero e inteiro")
    else:print("Numero e decimal")
if op=="-" :
    print("resultado =",r2)
    if (r2%2)==1:print("Número impar")
    elif (r2%2)==0:print("Número par")
    if r2>=0:print("valor e positivo")
    elif r2<0:print("valor e negativo")
    if r2%1==0:print("Numero e inteiro")
    else:print("Numero e decimal") 
if op=="*" : 
    print("resultado =",r3)
    if (r3%2)==1:print("Número impar")
    elif (r3%2)==0:print("Número par") 
    if r3>=0:print("valor e positivo")
    elif r3<0:print("valor e negativo")
    if r3%1==0:print("Numero e inteiro")
    else:print("Numero e decimal") 
if op=="/" :
    print("resultado =",r4)
    if (r4%2)==1:print("Número impar")
    elif (r4%2)==0:print("Número par") 
    if r4>=0:print("valor e positivo")
    elif r4<0:print("valor e negativo") 
    if r4%1==0:print("Numero e inteiro")
    else:print("Numero e decimal")

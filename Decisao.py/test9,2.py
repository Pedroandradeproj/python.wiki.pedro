# Programa que leia cinco números e mostre-os em ordem decrescente.print("Digite primeiro numero:")
print("Digite primeiro numero:")
n1=int(input())
print("Digite segundo numero:")
n2=int(input())
print("Digite terceiro numero:")
n3=int(input())
print("Digite quarto numero:")
n4=int(input())
print("Digite quinto numero:")
n5=int(input())
# verifica os 1
if n1 < n2:
    n1, n2 = n2, n1

if n1 < n3:
    n1, n3 = n3, n1

if n1 < n4:
    n1,n4=n4,n1

if n1 < n5:
   n1,n5=n5,n1 
# verifica os 2

if n2 < n3:
    n2, n3 = n3, n2

if n2 < n4:
    n2, n4 = n4, n2

if n2 < n5:
   n2,n5=n5,n2 
# verifica os 3

if n3 < n4:
    n3, n4 = n4, n3

if n3 < n5:
   n3,n5=n5,n3
# verifica os 4

if n4 < n5:
   n4,n5=n5,n4

print(f'A ordem decrescente é {n1}, {n2}, {n3}, {n4} e {n5} ')
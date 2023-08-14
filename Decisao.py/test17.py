# Programa que peça um número correspondente a um determinado ano 
# e em seguida informe se este ano é ou não bissexto.
print("Informe número correspondente a um determinado ano :")
a=int(input())
if (a%4==0 and a%100!=0) or (a%400==0): print("ano é bissexto")
else :print("não e bissexto")
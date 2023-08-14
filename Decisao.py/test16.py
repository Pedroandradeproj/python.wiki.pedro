#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
# O programa deverá pedir os valores de a, b e c e fazer as consistências,
# informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau
# e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
print("Informe valores de a")
a=float(input())
print("Informe valores de b")
b=float(input())
print("Informe valores de c")
c=float(input())
print("calcular o valor de delta:")
x=(a*a)+b+c # calcula as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
print(x)
if a==0 : print("a equação não é do segundo grau")
elif x<0: print("a equação não possui raizes reais")
elif x==0: print("a equação possui apenas uma raiz real")
elif x>0: print("a equação possui duas raiz reais")
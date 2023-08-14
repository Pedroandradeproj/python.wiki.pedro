#endo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# A)Para homens: (72.7*h) - 58
# B)Para mulheres: (62.1*h) - 44.7

print("Informe a altura para homen")
alt=float(input())
h=(72.7*alt)-58
print("Peso ideal para homen =",h)

print("Informe a altura mulher")
m=(62.1*alt)-44.7
print("Peso ideal para  mulher =",m)

# Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores
# podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero
# , isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;
print("Informe valor do primeiro lado do triangulo")
n1=float(input())
print("Informe valor do segundo lado do triangulo")
n2=float(input())
print("Informe valor do terceiro lado do triangulo")
n3=float(input())
if (n1+n2)<n3 and (n2+n3)<n1 and (n1+n3)<n2:
    print("Não e um Triângulo")
elif n1==n2==n3 :
    print("Triângulo Equilátero")
elif n1==n2 and n2==n3 and n1==n3:
    print("Triângulo Isósceles")
else : print("Triângulo Escaleno")   
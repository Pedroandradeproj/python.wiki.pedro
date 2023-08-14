# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo 
# de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
# "Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E
#  algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem
# “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
print("Informe Primeiro numero ?")
n1=int(input())
print("Informe Segundo numero ?")
n2=int(input())
m=(n1+n2)/2
if m>9 and m<=10:
    m="A"
elif m>=7.5 and m<9:
    m="B"
elif m>=6 and m<7.5:
    m="C"
elif m>=4 and m<6:
    m="D"
elif m>=0 and m<4:
    m="E"

if m=="A":
    print("APROVADO")
elif m=="B" :
    print("APROVADO")
elif m=="C":
    print("APROVADO")
elif m=="D":
    print("REPROVADO")
elif m=="E":
    print("REPROVADO")
# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A)A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# B)A mensagem "Reprovado", se a média for menor do que sete;
# C)A mensagem "Aprovado com Distinção", se a média for igual a dez.
print("Digite primeira nota :")
n1=int(input())
print("Digite seguunda nota :")
n2=int(input())
m=(n1+n2)/2
if (m>=7 and m<=9):
    print("Aprovado")
if (m>=0 and m<=6):
    print("Reprovado")
if (m>=10):
    print("Aprovado com Distinção")
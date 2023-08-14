# leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
# se digitar outro valor deve aparecer valor inválido.
print("Digite um numero conforme a ordem a ordem 1-Domingo, 2- Segunda, etc")
n=int(input())
if n==1:
    print("Domingo")
elif n==2:
    print("Segunda")
elif n==3:
    print("Terça feira")
elif n==4:
    print("Quarta feira")
elif n==5:
    print("Quinta feira")
elif n==6:
    print("Sexta feira")
elif n==7:
    print("Sabado")
elif n>=8:
    print("Numero invalido")
    
# Faça um programa que calcule o mostre a média aritmética de N notas.

qnotas=int(input("Informe quantidade de notas : "))
nota=0
for i in range (qnotas):
    nota+=int(input("Informe notas : "))   
    
media=nota/qnotas
print(f"A media de {qnotas} notas e : {media}")


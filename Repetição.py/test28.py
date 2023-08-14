# Faça um programa que calcule o valor total investido por um colecionador
# em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário 
# deverá informar a quantidade de CDs e o valor para em cada um.

qtdcds=int(input("Informe a quantidade de CDs : "))

qcds=0

for i in range (qtdcds):
    cds=int(input("Informe valor do CDs: "))
    qcds+=cds  
 
media=qcds/qtdcds

print(f"o valor total investido por um colecionador em sua coleção de CDs : R$ {qcds}")
print(f"o valor médio gasto em cada um deles : R$ {media}")
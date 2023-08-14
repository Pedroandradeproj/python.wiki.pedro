# pedir o tamanho em metros quadrados da área a ser pintada, considere que a cobertura da tinta é de 1 litro para 
# cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.


print("Informe o tamanho em metros quadrados da área a ser pintada ?")
m2=float(input())
qtdtinta=m2/3
qtdtinta=qtdtinta*1

latas=(qtdtinta/18)+1
print("Quantidades de latas de tinta a serem compradas")
print (int(latas))

valor=latas*80
print("valor total")
print (int(valor))
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga 
# e sempre arredonde os valores para cima, isto é, considere latas cheias.

print("Bom dia, Informe o tamanho em metros quadrados da área a ser pintada ?")
m2=int(input())
qtdtinta=m2/6
qtdtinta=qtdtinta*1.01

print("Ok,serão",m2,("m²"))
print("Voce vai precisar de",qtdtinta,"Litros de tinta")
print("Você prefere comprar ?")
print("Orçamento")
galoes=int(qtdtinta/3.6)+1
latas=int(qtdtinta/18)+1

print("Você prefere comprar ?")


print("Latas 18L:",latas,"un")
valor=latas*80.00
print("- Total:R$",valor)

print("Galoes 3.6L:",galoes,"un")
valor=galoes*25.00
print("- Total:R$",valor)

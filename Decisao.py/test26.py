# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, 
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a 
# ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
print("Selecione o tipo de combustivel, A-álcool ou G-gasolina ?")
combustivel=input()
# P= preço
# D= desconto
if combustivel=="A" :
    print("Informe quantos litros deseja :")
    a=float(input())
    if a<=20 :
        p=a*1.90
        d=p-(0.3*p)
        print("A-álcool R$ ",d)
    elif a>20 :
        p=a*1.90
        d=p-(0.5*p)
        print("A-álcool R$ ",d)       
elif combustivel=="G" :
    print("Informe quantos litros deseja :")
    g=float(input())
    if g<=20 :
        p=g*2.50
        d=p-(0.4*p)
        print("G-gasolina R$ ",d)
    elif g>20 :
        p=g*2.50
        d=p-(0.6*p)
        print("G-gasolina R$ ",d)   

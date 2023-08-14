# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda 
# um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a 
# quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
print("Informe quantos (Kg) de morangos :")
mo=float(input())
print("Informe quantos (Kg) de maças :")
ma=float(input())
# p==preço
if mo<=5:
    pmo=2.50*mo
    print(f"Morango         R${pmo} por Kg")   
elif mo >5:
    pmo=2.20*mo
    print(f"Morango         R${pmo} por Kg")
if ma<=5:
    pma=1.80*mo  
    print(f"Maçã            R${pma} por Kg")
elif ma >5:
    pma=1.50*mo 
    print(f"Maçã            R${pma} por Kg")

tf=ma+mo
tp=pma+pmo
if tf>8 or tp>25:
    tp=tp-(0.10*tp)
    print(f"Total            R${tp}")
else:print(f"Total           R${tp}")
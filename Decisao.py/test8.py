# programa que pergunte o preço de três produtos e informe qual produto 
# você deve comprar, sabendo que a decisão é sempre pelo mais barato.
print("informe preço do primeiro produto")
p1=float(input())
print("informe preço do segundo produto")
p2=float(input())
print("informe preço do terceiro produto")
p3=float(input())
#informa o produto com menor preço
if(p1<p2 and p1<p3):
    print("O mais em conta : ",p1)
if(p2<p1 and p2<p3):
    print("O mais em conta : ",p2)
if(p3<p1 and p3<p2):
    print("O mais em conta : ",p3) 
    



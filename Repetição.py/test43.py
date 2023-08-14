# O cardápio de uma lanchonete é o seguinte: 
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral
# do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado
rep=1
ped=[]
tg=0.0
qtp=0
ped.append("Especificação      Código        Preço       qtd      ptp")
while rep>0:
    cod=int(input("Informe código do produto : "))
    qtdd=int(input("Informe quantidade desejada : "))
    if cod==0 :
        rep-=1
    elif cod==100 :
        qtp=float(1.20*qtdd)
        tg+=qtp
        ped.append(f"Cachorro Quente      100        R$ 1,20       {qtdd}      R$ {qtp:.2f}")
    elif cod==101 :
        qtp=float(1.30*qtdd)
        tg+=qtp
        ped.append(f"Bauru Simples        101        R$ 1,30       {qtdd}      R$ {qtp:.2f}")    
    elif cod==102 :
        qtp=float(1.50*qtdd)
        tg+=qtp
        ped.append(f"Bauru com ovo        102        R$ 1,50       {qtdd}      R$ {qtp:.2f}")    
    elif cod==103 : 
        qtp=float(1.20*qtdd)
        tg+=qtp
        ped.append(f"Hambúrguer           103        R$ 1,20       {qtdd}      R$ {qtp:.2f}") 
    elif cod==104 :
        qtp=float(1.30*qtdd)
        tg+=qtp
        ped.append(f"Cheeseburguer        104        R$ 1,30       {qtdd}      R$ {qtp:.2f}")    
    elif cod==105 :
        qtp=float(1.00*qtdd)
        tg+=qtp
        ped.append(f"Refrigerante         105        R$ 1,00       {qtdd}      R$ {qtp:.2f}")                                                                                         
print(*ped, sep = "\n")
print             (f"total geral do pedido                                R$ {tg:.2f}")
# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara 
# o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo
# e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: 
# tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
print("Informe tipo de carne: fp-File Duplo, a-Alcatra ou p-Picanha ")
tpc=input("")
print("Informe quandidade de carne :")
qdc=float(input())
print("Infome tipo de pagamento: ct-cartão Tabajara ou ot-outros")
tp=input("")
if tpc=="fp" :
    print(f"qtdade de carne :           {qdc}")
    if qdc<=5:
        vp=qdc*4.90
    elif qdc>5:
        vp=qdc*5.80
    print(f"File Duplo               R$ {vp} por Kg")
    print(f"Total a pagar            R$ {vp}")
    if tp=="ct":
        d=vp*0.05
        print(f"valor do Desconto          R$ {d}")
        vp=vp-(vp*0.05)
        print(f"Valor a pagar              R$ {vp}")
    elif tp=="ot":
        print(f"Valor a pagar              R$ {vp}")        

elif tpc=="a" :
    print(f"qtdade de carne :           {qdc}")
    if qdc<=5:vp=qdc*5.90
    elif qdc>5:vp=qdc*6.80 
    print(f"Alcatra                  R$ {vp} por Kg")
    print(f"Total a pagar            R$ {vp}")
    if tp=="ct":
        d=vp*0.05
        print(f"valor do Desconto          R$ {d}")
        vp=vp-(vp*0.05)
        print(f"Valor a pagar              R$ {vp}") 
    elif tp=="ot":
        print(f"Valor a pagar              R$ {vp}")       


elif tpc=="p" :
    print(f"qtdade de carne :           {qdc}")
    if qdc<=5:vp=qdc*6.90
    elif qdc>5:vp=qdc*7.80  
    print(f"Picanha                  R$ {vp} por Kg")
    print(f"Total a pagar            R$ {vp}")
    if tp=="ct":
        d=vp*0.05
        print(f"valor do Desconto        R$ {d}")
        vp=vp-(vp*0.05)
        print(f"Valor a pagar            R$ {vp}")
    elif tp=="ot":
        print(f"Valor a pagar            R$ {vp}")    

# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os 
# seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
vali=float(input("Digite valor inicial : "))
lista=[]
qtdpar=1
qtdp=4
vj=0
n=3
vlpar=vali
esp1="                    "
esp2="                  "
print(" Valor da Dívida      Valor dos Juros   Quantidade de Parcelas   Valor da Parcela")
print(f"    R$ {vali:.2f}             {vj}{esp1}{qtdpar}{esp2}R$ {vlpar:.2f}")
vj1=100
for i in range(qtdp): 
    qtdpar=1*n
    vali+=50
    vlpar=vali/qtdpar
    if vj1>9 and vj1<100:
        esp1="                   "
    if vj1>99 and vj1<1000:
        esp1="                  "    
    if qtdpar>9 and qtdpar<100:
        esp2="                 "    
    lista.append(f"    R$ {vali:.2f}             {vj1}{esp1}{qtdpar}{esp2}R$ {vlpar:.2f}")
    vj1+=50      
    n+=3
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

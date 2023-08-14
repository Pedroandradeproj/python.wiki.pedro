# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
# Foram obtidos os seguintes dados:
# Código da cidade;
# Número de veículos de passeio (em 1999);
# Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# Qual a média de veículos nas cinco cidades juntas;
# Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
medc=0
tcid=5
melist1=[]
malist2=[]
mda=0
cmda=0
ma=[]
me=[]
for i in range(tcid):
    codc=input("Informe Código da cidade : ") 
    numv=float(input("Informe números de veículos passeio da cidade : "))
    numa=float(input("Informe Número de acidentes de trânsito com vítimas : "))
    melist1.append(numa)
    malist2.append(numa)
    ma.append(codc)
    me.append(codc)
    if melist1[0]>numa:
        melist1[0]=numa 
        me[0]=codc     
    if malist2[0]<numa:
        malist2[0]=numa
        ma[0]=codc 
    medc+=numv
    if numa<=2000:
       mda+=numa
       cmda+=1
print(f"maior índice de acidentes de transito é {malist2[0]} da cidade {ma[0]}")       
print(f"menor índice de acidentes de transito é {melist1[0]} da cidade {me[0]}")       
print(f"A média de veículos nas cinco cidades juntas M= {(medc/tcid):.2f}")
print(f"a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio M= {(mda/cmda):.2f}")
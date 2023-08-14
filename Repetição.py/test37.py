# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, 
# o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que
# pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O 
# final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo
# código. Ao encerrar o programa também deve ser informados os códigos e valores do 
# cliente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das
# alturas e dos pesos dos clientes

lista=1
dados=[]
maalt=[]
mapes=[]
mealt=[]
mepes=[]
cliente=float(0)
mp=0
ma=0
maiorA=[]
menorA=[]
maiorP=[]
menorP=[]

while lista>0:
    cod=int(input("informe seu código : "))
    cod1=float(input("informe sua altura  : "))
    cod2=float(input("informe seu peso : "))
    dados1= (f"código : {cod}  altura : {cod1:.2f}  peso : {cod2:.1f}")
    dado=dados1
    maalt.append(cod1)
    mapes.append(cod2)
    mealt.append(cod1)
    mepes.append(cod2) 
    
    maiorA.append(dados1)
    menorA.append(dados1)
    maiorP.append(dados1)
    menorP.append(dados1) 
    
    
    if (cod==0 and cod1==0 and cod2==0):
        lista-=1       
    if lista==1 :    
        cliente+=1
        mp+=cod2
        ma+=cod1
        if maalt[0]<cod1:
            maalt[0]=cod1
            maiorA[0]=dados1      
        if mealt[0]>cod1:
            mealt[0]=cod1
            menorA[0]=dados1                    
        if mapes[0]<cod2:       
            mapes[0]=cod2
            maiorP[0]=dados1
        if mepes[0]>cod2:       
            mepes[0]=cod2
            menorP[0]=dados1                                    
    elif lista==0:        
        mp=mp/cliente
        ma=ma/cliente
        print(f"cliente mais alto  : {maiorA[0]}")
        print(f"cliente mais baixo : {menorA[0]}")
        print(f"cliente mais gordo : {maiorP[0]}")
        print(f"cliente mais magro : {menorP[0]}")
        print(f"media de altura dos clientes: {ma:.2f}")
        print(f"media de peso dos clientes  : {mp:.2f}")                  
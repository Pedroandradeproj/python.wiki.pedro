# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um 
# programa que leia as um conjunto indeterminado de temperaturas, e informe 
# ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
lista=1
maior=[]
menor=[]
maior1=0
menor1=0
media=0
divisor=0
comp1=0
comp2=0

while lista>0:
    num=int(input("informe temperatura :" )) 
    maior.append(num)
    menor.append(num)
    
    divisor+=1
    if num==0:
        lista-=1
        media=media/(divisor-1)  
        print(f"média das temperaturas : {media:.2f}")
        print(f"maior temperatura : ",maior1)
        print(f"menor temperatura : ",menor1)
    if lista==1:
        if maior[0]<num:
            maior1=num 
            maior[0]=maior1             
        if menor[0]>num:
            menor1=num 
            menor[0]=menor1 
                   
    media+=num
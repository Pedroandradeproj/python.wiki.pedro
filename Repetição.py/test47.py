#Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e
# a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você 
# deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas
# pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima
# informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes).
# As notas não são informados ordenadas.

mainota=[]
mennota=[]
rep=1
resf=[]
cont=0
while rep>0:
    num=input("Atleta: ")
    if num=="":
        rep-=1
    else:
        cont+=1
        print("")
        s1=float(input("Nota: "))
        s2=float(input("Nota: "))
        s3=float(input("Nota: "))
        s4=float(input("Nota: "))
        s5=float(input("Nota: "))
        s6=float(input("Nota: "))
        s7=float(input("Nota: "))
        print("")
        maior=s1
        menor=s1
        mainota.append(f"Nota: {s1} m")
        mennota.append(f"Nota: {s1} m")
        if s2>maior:
            maior=s2
            mainota[0]=(f"Nota: {s2} ")
        if s3>maior:
            maior=s3
            mainota[0]=(f"Nota: {s3} ")
        if s4>maior:
            maior=s4
            mainota[0]=(f"Nota: {s4} ")    
        if s5>maior:
            maior=s5
            mainota[0]=(f"Nota: {s5} ")
        if s6>maior:
            maior=s6
            mainota[0]=(f"Nota: {s6} ")    
        if s7>maior:
            maior=s7
            mainota[0]=(f"Nota: {s7} ")               
        if s2<menor:
            menor=s2
            mennota[0]=(f"Nota: {s2} ")  
        if s3<menor:
            menor=s3
            mennota[0]=(f"Nota: {s3} ")      
        if s4<menor:
            menor=s4
            mennota[0]=(f"Nota: {s4} ")      
        if s5<menor:
            menor=s5
            mennota[0]=(f"Nota: {s5}")   
        if s6<menor:
            menor=s6
            mennota[0]=(f"Nota: {s6}")    
        if s7<menor:
            menor=s7
            mennota[0]=(f"Nota: {s7}")    
            
        print(f"Melhor Nota: {mainota[0]}")    
        print(f"Pior   Nota: {mennota[0]}")    
        media=((s1+s2+s3+s4+s5)-(menor+maior))/3        
        print(f"Média: {media:.2f}")  
        resf.append(f"{num} : {media:.2f}")
          
        print("")
print(f"Resultado final:")    
for i in range (cont):
    print(resf[i])
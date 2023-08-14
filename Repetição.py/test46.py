# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final 
# da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado
# fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as
# cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme 
# a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso 
# de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não 
# são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do
# programa deve ser conforme o exemplo abaixo:
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
        s1=float(input("Primeiro  Salto: "))
        s2=float(input("Segundo   Salto: "))
        s3=float(input("Terceiro  Salto: "))
        s4=float(input("Quarto    Salto: "))
        s5=float(input("Quinto    Salto: "))
        print("")
        maior=s1
        menor=s1
        mainota.append(f"Primeiro  Salto: {s1} m")
        mennota.append(f"Primeiro  Salto: {s1} m")
        if s2>maior:
            maior=s2
            mainota[0]=(f"Segundo   Salto: {s2} m")
        if s3>maior:
            maior=s3
            mainota[0]=(f"Terceiro  Salto: {s3} m")
        if s4>maior:
            maior=s4
            mainota[0]=(f"Quarto    Salto: {s4} m")    
        if s5>maior:
            maior=s5
            mainota[0]=(f"Quinto    Salto: {s5} m")
        if s2<menor:
            menor=s2
            mennota[0]=(f"Segundo   Salto: {s2} m")  
        if s3<menor:
            menor=s3
            mennota[0]=(f"Terceiro  Salto: {s3} m")      
        if s4<menor:
            menor=s4
            mennota[0]=(f"Quarto    Salto: {s4} m")      
        if s5<menor:
            menor=s5
            mennota[0]=(f"Quinto    Salto: {s5} m")   
        print(f"Melhor salto: {mainota[0]}")    
        print(f"Pior   salto: {mennota[0]}")    
        media=((s1+s2+s3+s4+s5)-(menor+maior))/3        
        print(f"Média dos demais saltos: {media:.2f}")  
        resf.append(f"{num} : {media:.2f}")
          
        print("")
print(f"Resultado final:")    
for i in range (cont):
    print(resf[i])
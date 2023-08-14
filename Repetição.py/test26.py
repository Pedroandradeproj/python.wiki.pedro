# Numa eleição existem três candidatos. Faça um programa que peça o número 
# total de eleitores. Peça para cada eleitor votar e ao final mostrar 
# o número de votos de cada candidato.

qelei=int(input("número total de eleitores : "))
can1=0
can2=0
can3=0
for i  in range(qelei):
    print("Digite o N do seu cantidado")
    print("candidato 1 =N.1 , candidato 2 =N.2 , candidato 3 =N.3  ")
    cantidado=int(input())
    while cantidado>3 or cantidado<1:
        print("Informe novamente seu cantidado")
        cantidado=int(input())
    if cantidado==1:
        can1+=1
    elif cantidado==2:
        can2+=1
    elif cantidado==3:
        can3+=1    
    
print(f"candidato 1, número de votos: {can1}")    
print(f"candidato 2, número de votos: {can2}")    
print(f"candidato 3, número de votos: {can3}")


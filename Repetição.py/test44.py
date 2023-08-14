#  Em uma eleição presidencial existem quatro candidatos. Os votos são informados
# por meio de código. Os códigos utilizados são
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
elei=int(input("Informe quantidade de eleitores: "))
c1=0
c2=0
c3=0
c4=0
c5=0
c6=0
for i in range (elei):
    print("1 - Enéas / 2- Bolsonaro/ 3- Samuel/ 4- Cleberson/ 5- voto nulo/ 6-voto em branco)")
    fot=int(input("Informe seu voto=  "))
    while fot=='1' or fot=='2' or fot=='3' or fot=='4' or fot=='5' or fot=='6':
        print("Informe seu voto corretamente")
        fot=int(input("Informe seu voto=  "))
    if fot==1:
        print(" voto confirmado : 1 - Enéas")
        c1+=1
    elif fot==2:
        print(" voto confirmado : 2- Bolsonaro ")
        c2+=1
    elif fot==3:
        print(" voto confirmado : 3- Samuel ")
        c3+=1
    elif fot==4:
        print(" voto confirmado : 4- Cleberson")
        c4+=1
    elif fot==5:
        print(" voto e nulo")
        c5+=1
    elif fot==6:
        print(" voto em branco")
        c6+=1
pn=(((c1+c2+c3+c4+c5+c6)*c5)/100)
pb=(((c1+c2+c3+c4+c5+c6)*c6)/100)
print(f"O total de votos para O candidato Enéas     : {c1} ")    
print(f"O total de votos para O candidato Bolsonaro : {c2} ")
print(f"O total de votos para O candidato Samuel    : {c3} ")
print(f"O total de votos para O candidato Cleberson : {c4} ")
print(f"O total de votos voto nulo                  : {c5} ")
print(f"O total de votos voto em branco             : {c6} ")
print(f"A porcentagem de votos nulos sobre o total de votos      : {pn:.2f}%")    
print(f"A porcentagem de votos em branco sobre o total de votos  : {pb:.2f}%")        

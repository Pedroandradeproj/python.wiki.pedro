#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
qtdcons=0
consoantes=[]
vetor = input("Digite algo com 10 caracteres : ")
if len(vetor)> 10: 
    print("Erro ...  tente novamente com 10 caracteres ok ")
    vetor = input("Digite algo com 10 caracteres : ")
for i in range(10):
    veri = vetor[i]
    if veri == "a" or veri == "e" or veri == "i" or veri == "o" or  veri =="u":
        qtdcons+=1
        consoantes.append(veri)
        
print(vetor)
print(f"quantidades de consoantes lidas : {qtdcons} ") 
if len(consoantes) >= 1:
    print(f"consoantes lidas : {consoantes}")
    


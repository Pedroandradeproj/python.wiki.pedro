# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
# Imprima a idade e a altura na ordem inversa a ordem lida.
idade=[]
altura=[]

for i in range(5):
    idade1=int(input("Informe idade : "))
    altura1=float(input("Informe altura : "))
    altura.append(altura1)
    idade.append(idade1)

print("Item informado na ordem inversa !")

for i in range(5):
    print(idade[4-i])
    print(altura[4-i])
    
#se for somente um lista de cada vez e so 
#for i in range(5):
#   print(idade[4-i])
#for i in range(5):
#    print(altura[4-i])
    
    
    
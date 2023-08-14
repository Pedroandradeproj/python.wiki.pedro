# Faça um programa que leia 5 números e informe o maior número.
# linha 7
lista = []
qtn = input("informe a qt de numeros: ")

for n in range(0,int(qtn)): 
    lista.append(int(input("Digite o número: ")))

print ("Maior número da lista: ", max(lista)) 
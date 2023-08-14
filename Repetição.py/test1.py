# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido 
# e continue pedindo até que o usuário informe um valor válido.
print("Digite uma nota")
n=int(input())
while n>10 or n<0:
    print ("valor Invalido")
    print("Digite uma nota")
    n=int(input())
else: print(f"valido = {n}") 
# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial 
# várias vezes e limitando o fatorial a números inteiros positivos e menores que 16
while True:
    fat=int(input("Informe número fatorial : "))
    while fat<0 or fat>16:
        print("numero fatorial nao pode ser negativo e menor que 16")
        fat=int(input("Informe número fatorial : "))
    
    cont=fat-1
    contm=[fat]
    mul=fat
    res=fat
    n=0
    for i in range (cont):
        mul-=1
        contm[0]=(f"{contm[0]}.{mul}")
        res*=mul
        print(f"{fat}!={contm[0]}={res}")



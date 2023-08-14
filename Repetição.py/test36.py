# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será
# digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar
# em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:

ntab=int(input("Montar a tabuada de: "))
ctab=int(input("Começar por: "))
ftab=int(input("Terminar em: "))
while ctab>=ftab:
    print("terminar ter que ser maior que começar")
    ftab=int(input("Terminar em: "))
    
lista=ftab-ctab+1
n=ctab
conta=0
print()
print(f"Vou montar a tabuada de {ntab} começando em {ctab} e terminando em {ftab}:")
for i in range (lista):
    conta=ntab*n
    print(f"{ntab} X {n} = {conta}")
    n+=1



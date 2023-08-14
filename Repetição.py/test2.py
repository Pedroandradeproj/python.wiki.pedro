# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome 
# do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
print("Digite nome")
n=input("")
print("Digite senha")
s=input("")
while n==s: 
    print("erro : nome e senha, não podem ser iguais")
    print("Digite nome")
    n=input("")
    print("Digite senha")
    s=input("")
else:print("concluido")
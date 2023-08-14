#O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia 
# da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver
# o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão
# informado pelo usuário, conforme o exemplo abaixo:

lista=50
valor=float(input("Preço do pão: R$ "))
n=0
valor1=0
print("panificadora Pão de Ontem - Tabela de preços")
for i in range(lista):
    valor1+=valor
    n+=1
    print(f"{n} - R$ {valor1:.2f}")
# Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do
# percentual do ano anterior. Faça um programa que determine o salário atual desse 
# funcionário. Após concluir isto, altere o programa permitindo que o usuário digite
# o salário inicial do funcionário.

sal1=float(input("o salário inicial do funcionário : "))
#!!! sal1=1000 antes
ano1=int(1995)
porc=0.0075
ano=int(input(F"ano de verificação do salario : "))
while ano<1995:
    ano=int(input(F"ano de verificação do salario : "))
rep=ano-ano1
for i in range (rep):
    porc*=2
    sal1+=sal1*porc
print(F"Em {ano} recebeu aumento de {porc*100} sobre seu salário inicial")
print(f"Salario do ano {ano} é : R$ {sal1}")


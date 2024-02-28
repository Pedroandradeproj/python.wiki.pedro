# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
#  Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e
#   5 como "Assassino". Caso contrário, ele será classificado como "Inocente".]
list=[
"Telefonou para a vítima? ",
"Esteve no local do crime? ",
"Mora perto da vítima? ",
"Devia para a vítima? ",
"Já trabalhou com a vítima? "
]
cont=0
print("responda com sim ou nao minusculo")
for i in range(5):
    print(list[i])
    veri = input()
    if veri == "sim":
        cont+=1
if cont == 1 : 
    print("inocente")
if cont == 2 : 
    print("suspeito")
if cont == 3 or cont == 4  : 
    print("cúmplice")    
if cont == 5 : 
    print("assassino")
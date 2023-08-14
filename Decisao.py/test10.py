#Faça um Programa que pergunte em que turno você estuda. Peça para digitar 
# M-matutino ou V-pertino ou N- Noturno. Imprima a mensagem "Bom Dia!", 
# "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
print("informe uma das tres opções : M-matutino ou V-Vespertino ou N- Noturno")
print("Em que turno você estuda ?  ")
tn=input()
if tn==("M-matutino"): 
    print("Bom Dia!")
elif tn==("V-pertino"):
    print("Boa Tarde!")
elif tn==("N-Noturno"):
    print("Boa Noite!")
if tn==("M"): 
    print("Bom Dia !")
elif tn==("V"):
    print("Boa Tarde!")
elif tn==("N"):
    print("Boa Noite!")
else : print("Valor Inválido!")
# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro
# entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída 
# deve ser conforme o exemplo abaixo:]
print("Informe o numero ")
ni=int(input())
mul=0
print(f"Tabuada de {ni}")
while mul<10:
    mul+=1
    res=ni*mul
    print(f"{ni} X {mul} = {res}")
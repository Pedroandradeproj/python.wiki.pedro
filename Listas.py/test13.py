#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
# e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

vetor=[]
vetor_mes = ["1 - janeiro", "2 - fevereiro", "3 - março", "4 - abril", "5 - maio", "6 - junho",
             "7 - julho", "8 - agosto", "9 - setembro", "10 - outubro", "11 - novembro", "12 - dezembro"]
cal=0
for i in range(12):
    media = float(input("Informe a média de " + vetor_mes[i] + ": "))
    vetor.append({"mês": vetor_mes[i], "média": media})
    cal+=media
cal/=12
print(f"media : {media}")
for i in range (12):
    if vetor[i]["média"] >= cal : 
        print(vetor[i])

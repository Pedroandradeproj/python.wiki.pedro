# programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
# (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)

print("Informe o tamanho de um arquivo para download (em MB) ?")
tam=int(input())

print("Informe velocidade de um link de Internet (em Mbps) ?")
vel=int(input())

bits=tam*8
tempo=bits/vel
min=int(tempo/60)

print("velocidade de download em minuto = ",min)
# Faça um programa que peça para n pessoas a sua idade, ao final o programa 
# devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 
# e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, 
# conforme a média calculada.

qpessoas=int(input("Informe quantidade de pessoas : "))
media1=0
for i in range(qpessoas):
    idade=int(input("Informe idade : "))
    while idade<0 or idade>160:
        print("Pelo amor de Deus digite a idade correta")
        idade=int(input("Informe idade : "))
    media1+=idade

media=media1/qpessoas    

if media >=0 and media<=25:
    print(f"turma é jovem, media={media}")

if media >=26 and media<=60:
    print(f"turma é adulta, media={media}")

if media >60:
    print(f"turma é idosa, media={media}")


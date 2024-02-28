# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando 
# a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta 
# entrada de dados, faça:
# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;

cont=1
some=0
valores=[]
acimamedia=[]
somemedia=0
somesete=0
qtdsete=[]
while cont == 1:
    valor=int(input("Informe um valor : "))
    if valor == -1 :
        cont-=1
    else:
        valores.append(valor)
        some+=valor

media=some/(len.valores + 1)
print(f"Quantidade de valores que foram lidos : {len.valores}")
print(f"valores na ordem em que foram informados, um ao lado do outro :{valores}")

for i in range (len.valores):
    cont=len.valores
    print(valores[cont])
    cont-=1

print(f"a soma dos valores {some}")
print(f"a média dos valores {media}")

for i in range(len.valores):
    if valores[i] >= media :
        somemedia+=valores[i]
        acimamedia.append(valores[i])
    if valores[i] <= 7:
        somesete+=valores[i]
        qtdsete.append(valores[i])
        


print(f"Calculo dos que estão acima da media  = {somemedia} e a quantidade de valores acima da média :  {len.acimamedia}")
print(f"Calculo dos que são menores que 7 = {somesete} e a quantidade de valores abaixo de sete : {qtdsete}")

print("                         Fim ")
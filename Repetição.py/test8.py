# Faça um programa que leia 5 números e informe a soma e a média dos números
quant = 5
count = 0
maior = 1
for i in range(quant):
    numero = int(input('Informe um número: '))
    count += numero
if numero > maior:
    maior = numero
print('Total da soma: ', count)
print('Maior número: ', maior)
print('Média: %.2f' % (count / quant))

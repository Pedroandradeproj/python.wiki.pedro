# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa que gere a série até que o valor seja maior que 500


fib=[0,1]
n=0
n1=1
nf=1

while 500>fib[nf]:
    num=fib[n]
    num1=fib[n1]
    fib.append(num+num1)
    n+=1
    n1+=1
    nf+=1
print(fib)
# em fez de nf pode ser -1 pra chamar um ultimo item da lista

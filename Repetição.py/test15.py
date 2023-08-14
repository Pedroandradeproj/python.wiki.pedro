# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um
# programa capaz de gerar a série até o n−ésimo termo

rep=int(input("Quantas numeros da série de Fibonacci : "))
fib=[0,1]
n=0
n1=1
for i in range (rep):
    num=fib[n]
    num1=fib[n1]
    fib.append(num+num1)
    n+=1
    n1+=1

print(fib)


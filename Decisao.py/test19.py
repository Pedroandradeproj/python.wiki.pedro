# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade
# de centenas,dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301,
# 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
print("informe numero inteiro menor que 1000")
n=int(input())
u=int(n%10)
d=int(((n-u)/10)%10)
c=int((n-(d*10+u))/100)
if n<1000 and n>=100: print(c,"centenas,",d," dezenas e",u,"unidades")
elif n<100 and n>=10: print(d,"dezenas e",u,"unidades")
elif n<10  and n>1: print(u,"unidades") 
else : print("Informe numero maior que 1000 e maior que 0")
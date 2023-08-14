# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.



ano=0
a=int(input("População do país A: "))
while a<0:
    a=int(input("População do país deve ser maior que 0: "))
tdca=float(input("Taxa de crescimento da cidade A: "))

b=int(input("População do país B: "))
while b<0:
    b=int(input("População do país deve ser maior que 0: "))
tdcb=float(input("Taxa de crescimento da cidade B: "))

while a<b:
    a=a+(a*(tdca/100))
    b=b+(b*(tdcb/100))
    ano=ano+1
print("População do país",a)
print("População do país",b)
print("o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B :",ano)


# ou como prof falou a+=a*b
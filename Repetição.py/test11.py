# Altere o programa anterior para mostrar no final a soma dos números.
num1=int(input("digite um numero "))
num2=int(input("digite outro numero "))
while num2<num1:
    print("primeiro numero tem que ser menor que o segundo numero")
    num1=int(input("digite um numero "))
    num2=int(input("digite outro numero "))
else:
	for i in range(num1,num2,1):
		print(i)
print("resultado da soma dos dois numeros = ",num1+num2)  

# segundo jeito
while num2>=num1 :
    print(num2)
    num2-=1
    


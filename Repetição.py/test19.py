# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

qn=int(input("Informe quatidade de numero desejados : "))
num=int(input("informe numero :" ))
while num<0 or num>100:
    print("o programa aceita apenas números entre 0 e 1000.")
    num=int(input("informe numero :" ))
soma=num
maior=num
menor=num
qn-=1
for i in range (qn):
    num=int(input("informe numero :" )) 
    if maior<num:
        maior=num              
    if menor>num:
        menor=num         
    soma+=num
    
print(f"soma dos valores : ",soma)
print(f"o maior valor : ",maior)
print(f"menor valor : ",menor)
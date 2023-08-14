# programa que leia a variável peso (peso de peixes) e calcule o excesso.
print("Informe peso dos peixes?")
p=int(input()) 

if   (p<=50) : 
 print ("Peixes esta dentro do limite")
 print(p)
 
if (p>50) :
 excesso=int(p-50)*4
 print ("Multa por excesso e")
 print (excesso)
 multat=excesso+p
 print("Total da multa")
 print(multat)
 
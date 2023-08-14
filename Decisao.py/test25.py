#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da 
# pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita"
# , entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"
print("Responda as perguntas com s =sim ou n=não")
p1=input("Telefonou para a vítima ? ")
p2=input("Esteve no local do crime ? ")
p3=input("Mora perto da vítima ? ")
p4=input("Devia para a vítima ? ")
p5=input("Já trabalhou com a vítima ? ")
if p1=="s" and p2=="s" and p3=="s" and p4=="s" and p5=="s" : print("Assassino !!!")
elif p1=="n": print("Cúmplice") 
elif p2=="n": print("Cúmplice") 
elif p3=="n": print("Cúmplice") 
elif p4=="n": print("Cúmplice")
elif p5=="n": print("Cúmplice") 
elif p1=="n" and p2=="n": print("Cúmplice")  
elif p1=="n" and p3=="n": print("Cúmplice")  
elif p1=="n" and p4=="n": print("Cúmplice")  
elif p1=="n" and p5=="n": print("Cúmplice") 
elif p2=="n" and p3=="n": print("Cúmplice")  
elif p2=="n" and p4=="n": print("Cúmplice")
elif p2=="n" and p5=="n": print("Cúmplice")
elif p3=="n" and p4=="n": print("Cúmplice")
elif p3=="n" and p5=="n": print("Cúmplice")
elif p4=="n" and p5=="n": print("Cúmplice")  
elif p1=="n" and p2=="n" and p3=="n" : print("Suspeita")  
elif p1=="n" and p2=="n" and p4=="n" : print("Suspeita")  
elif p1=="n" and p2=="n" and p5=="n" : print("Suspeita")  
elif p1=="n" and p3=="n" and p4=="n" : print("Suspeita")  
elif p1=="n" and p3=="n" and p5=="n" : print("Suspeita")
elif p1=="n" and p4=="n" and p5=="n" : print("Suspeita") 
elif p2=="n" and p3=="n" and p4=="n" : print("Suspeita")  
elif p2=="n" and p3=="n" and p5=="n" : print("Suspeita")
elif p2=="n" and p4=="n" and p5=="n" : print("Suspeita") 
elif p3=="n" and p4=="n" and p5=="n" : print("Suspeita")
else:print("Inocente") 

   
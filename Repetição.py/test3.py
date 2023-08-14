# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';
nom=input("Digite nome: ")
ida=int(input("Digite idade: "))
sen=int(input("Digite salario: "))
sex=input("Sexo: f ou m: ")
est=input("Estado Civil: s, c, v, d: ")
# Len () é uma função integrada ao Python que é utilizada para obter o número de itens em um 
# determinado objeto, string, array, listas, entre outros
while len (nom)<3: 
    nom=input("Digite nome")
while ida<0 and ida>150:
    ida=int(input("Digite idade"))  
while sen<0:
    sen=int(input("Digite senha"))
while (sex!= 'f') and (sex!='m'):
    sex=input("Sexo: f ou m: ") 
while (est!='s')and(est!='c')and(est!='v')and(est!='d'):
    est = input("Deve ser s, c, v ou d: ")
 #colocar '' ,se nao da errado em letra, nao tentar, nao tentar mesmo
 # !!! nao coloque "" em letra 
 #obs "!!!" fica vermelho = muito importante
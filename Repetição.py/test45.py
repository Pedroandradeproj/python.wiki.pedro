# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o 
# programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o 
# gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa)
# . Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema.
# Após todos os alunos terem respondido informar:
# Maior e Menor Acerto;
# Total de Alunos que utilizaram o sistema;
# A Média das Notas da Turma
main=[]
mn=[]
menn=[]
me=[]
rep=1
medn=0   # Média das Notas da Turma
tas=0    # Total de Alunos que utilizaram o sistema

while rep>0:
    nota=int(0)
    tas+=1
    alun=input("Nome aluno: ")
    print("Informe seu cabarito")
    print("Responder cabarito somente com ( a, b, c, d, e )")
    r1=input("Questão 1   =  ")    
    r2=input("Questão 2   =  ")     
    r3=input("Questão 3   =  ")     
    r4=input("Questão 4   =  ")     
    r5=input("Questão 5   =  ")     
    r6=input("Questão 6   =  ")     
    r7=input("Questão 7   =  ")     
    r8=input("Questão 8   =  ")     
    r9=input("Questão 9   =  ")     
    r10=input("Questão 10  =  ")   
    menn.append(f"Aluno {alun} Nota = {nota}")
    main.append(f"Aluno {alun} Nota = {nota}")      
    if r1=='a':
        nota+=1
    if r2=='b':
        nota+=1
    if r3=='d':
        nota+=1
    if r4=='c':
        nota+=1 
    if r5=='d':
        nota+=1           
    if r6=='b':
        nota+=1    
    if r7=='e':
        nota+=1    
    if r8=='a':
        nota+=1     
    if r9=='e':
        nota+=1     
    if r10=='c':
        nota+=1      
    medn+=nota
    print(f"Aluno {alun} Nota = {nota}")   
  
    me.append(nota)
    mn.append(nota)
    if mn[0]<=nota:
        mn[0]=nota
        main[0]=(f"Maior Nota : Aluno {alun} Nota = {nota}")
    if me[0]>=nota:
        me[0]=nota
        menn[0]=(f"Menor Nota : Aluno {alun} Nota = {nota}")      
    print("Se utilizar  o sistema novamente ")
    print("Digite S - sim    N - não")
    trep=input("Utilizar o sistema novamente : ")
    if trep=="N": 
        rep-=1        
medn/=tas
print(f"Total de Alunos que utilizaram o sistema : {tas}")
print(f"Media da turma = {medn:.2f}")
print(main[0])
print(menn[0])


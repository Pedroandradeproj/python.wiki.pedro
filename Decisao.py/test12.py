# um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são 
# do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o 
# Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o 
# valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme
# o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
print("Quanto você ganha por hora ?")
ph=float(input())
print("Número de horas trabalhadas no mês ?")
htm=float(input())
st=htm*ph # valotr total (st)

if st>0 and st<=900: 
    ir=0
elif st>900 and st<=1500:
    ir=st*0.05
elif st>1500 and st<=2500:
    ir=st*0.10
elif st>2500 :
    ir=0.20

inss=st*0.08 # Instituto Nacional do Seguro Social (INSS)
sdct=st*0.05 # Sinticato (sdct)
sl=st-(ir+inss) # Salario liguido (sl)
td=inss+ir

if ir==0:
    ir=(" Isento ")
    
print(f"""
+ Salário Bruto                  : R${st}
- IR (11%)                       : R${ir}
- INSS (8%)                      : R${inss}
- Sindicato ( 5%)                : R${sdct}
- Total de descontos             : R${td}        
= Salário Liquido                : R${sl}
""")
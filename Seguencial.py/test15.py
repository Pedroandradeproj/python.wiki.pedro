# Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total
# do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS 
# e 5% para o sindicato.

print("Quanto você ganha por hora ?")
ph=float(input())
print("Número de horas trabalhadas no mês ?")
htm=float(input())
st=htm*ph # valotr total (st)

ir=st*0.11 # imposto de Renda (ir)
inss=st*0.08 # Instituto Nacional do Seguro Social (INSS)
sdct=st*0.05 # Sinticato (sdct)
sl=st-(sdct+ir+inss) # Salario liguido (sl)


print(f"""
+ Salário Bruto : R${st}
- IR (11%) : R${ir}
- INSS (8%) : R${inss}
- Sindicato ( 5%) : R${sdct}
= Salário Liquido : R${sl}
""")
# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores 
# e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
# baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
print("Informe salário do colaborador :")
sc=float(input()) # salário antes do reajuste
print("salário antes do reajuste: ",sc)
if  sc>0 and sc<=280:
    sa=sc*0.20
    print("aumento de 20%  : R$",sc)
    sc=sc+sa
    print("valor do aumento : R$",sc)
elif  sc>280 and sc<=700:
    sa=sc*0.15
    print("aumento de 15% : R$",sa)
    sc=sc+sa
    print("valor do aumento : R$",sc)
elif  sc>700 and sc<=1500:
    sa=sc*0.10
    print("aumento de 10% : R$",sa)
    sc=sc+sa
    print("valor do aumento : R$",sc)
elif  sc>1500:
    sa=sc*0.05
    print("aumento de 5% : R$",sa)
    sc=sc+sa
    print("valor do aumento : R$",sc)
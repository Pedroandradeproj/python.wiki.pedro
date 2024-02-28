#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
# Criando um vetor (lista) vazia para armazenar os números
vetor = []

# Pedindo ao usuário para inserir 10 números reais
for i in range(10):
    numero = float(input(f"Digite o {i+1}º número real: "))
    vetor.append(numero)  # Adicionando o número à lista

# Invertendo a ordem dos números no vetor
vetor.reverse()

# Mostrando os números armazenados no vetor na ordem inversa
print("Números no vetor (ordem inversa):")
for num in vetor:
    print(num)

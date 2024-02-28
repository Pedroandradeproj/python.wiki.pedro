# Criando um vetor (lista) vazia para armazenar os números
vetor = []

# Pedindo ao usuário para inserir 5 números inteiros
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor.append(numero)  # Adicionando o número à lista

# Mostrando os números armazenados no vetor
print("Números no vetor:")
for num in vetor:
    print(num)

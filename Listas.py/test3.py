# Criando uma lista vazia para armazenar as notas
notas = []

# Pedindo ao usuário para inserir 4 notas
for i in range(4):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)  # Adicionando a nota à lista

# Calculando a média das notas
media = sum(notas) / len(notas)

# Mostrando as notas e a média na tela
print("Notas inseridas:")
for i, nota in enumerate(notas, start=1):
    print(f"Nota {i}: {nota}")

print(f"Média das notas: {media}")

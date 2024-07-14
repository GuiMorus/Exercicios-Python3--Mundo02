# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
# e que se encontram no intervalo de 1 até 500

# Variável do valor inicial da soma
soma = 0

# Repetindo os números para encontrar somente os ímpares
for n in range(1, 501, 2):
    # Verificando os ímpares
    if n % 3 == 0:
        # Somando os ímpares
        soma = soma + n

# Mostrando a soma
print("Os ímpares de 1 até 500 que são múltiplos de 3")
print(f"tem a soma = {soma}")

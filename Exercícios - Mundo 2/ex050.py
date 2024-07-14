# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
# que forem pares. Se o valor digitado for ímpar, desconsidere-o

# Iniciando variáveis
lista = []
soma = 0

# Repetição para inserir valores na lista
for c in range(0, 6):
    num = float(input(f"Digite o {c + 1}° número: "))
    lista.append(num)

# Repetição para verificar e somar números pares
for c in range(0, 6):
    par = lista[c]
    # Verificando os pares
    if par % 2 == 0:
        soma = soma + par

# Mostrando o resultado da soma
print(f"A soma dos números pares é igual a {soma}")

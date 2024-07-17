# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros
# elementos de uma sequência de Fibonacci.

# Variável resgatando quantidade de termos
termo = int(input("Quantos termos quer da sequência de Fibonacci: "))
termo -= 2

# Laço realizando a sequência de Fibonacci
c = 0
n = 0  # primeiro termo
n2 = 1  # segundo termo
fibonacci = n + n2  # terceiro termo
print("Fibonacci: 0 > 1", end="")

while c < termo:
    # Mostrando a sequência
    print(" >", fibonacci, end="")

    # Calculando Fibonacci
    n = n2  # segundo termo passa a ser o primeiro termo
    n2 = fibonacci  # terceiro termo passa ser o segundo termo
    fibonacci = n + n2  # novo terceiro termo
    c += 1  # acrescentando contador

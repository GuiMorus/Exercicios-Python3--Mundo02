# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

# Variável recolhendo valor
num = int(input("Digite um número para saber se é primo: "))

# Verificando primo
primo = True
for c in range(2, num):
    if num % c == 0:
        primo = False

# Mostrando resultado
if primo or num == 1 or num == 2:
    print(f"O número {num} é primo")
else:
    print("O número não é primo")

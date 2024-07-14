# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão aritmética

# Variáveis resgatando o 1º termo e a razão
termo = int(input("Digite o valor do 1° termo(a₁): "))
r = int(input("Digite o valor da razão(r): "))

# Repetição realizando os 10 primeiros termos e mostrando-os
print("Os 10 primeiros termos são (", end="")
for c in range(1, 11):
    print(termo, end=", ")
    termo += r

print("...)")   # Final do print

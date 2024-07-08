# Escreva um programa que leia dois números inteiros e compare-os mostrando na tela:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

# Variáveis resgatando os números
num = float(input("Digite um número: "))
num2 = float(input("Digite outro: "))

# Mostrando a mensagem para o usuário
if num > num2:
    print("O primeiro valor é maior")
elif num2 > num:
    print("O segundo valor é maior")
else:
    print("Não existe valor maior, os dois são iguais")

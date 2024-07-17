# Faça um programa que leia um número qualquer e mostre o seu fatorial

# Variável recolhendo número para fatorar
num = int(input("Digite um número para fatorar: "))

# Iniciando variáveis
resultado = num
texto = str(num)
first = num

# Laço fatorando o número
while not num == 1:
    resultado *= (num - 1)
    num -= 1
    texto = texto + f" x {num}"

# Mostrando resultado
print(f"{first}! = {texto} = {resultado}")

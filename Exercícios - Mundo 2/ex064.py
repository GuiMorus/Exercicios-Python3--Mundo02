# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai
# parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles
# desconsiderando o flag

# Iniciando variáveis
soma = 0

# Mensagem inicial
num = int(input("Digite um número: "))
print("Insira \033[32m999\033[m para sair do programa")

# Laço calculando os números
while not num == 999:
    soma += num
    num = int(input("Digite outro número: "))

# Mostrando resultado
print(f"Soma total dos números: {soma}")

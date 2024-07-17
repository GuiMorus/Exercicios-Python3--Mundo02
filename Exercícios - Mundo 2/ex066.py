# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
# o usuário digitar 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles

# Iniciando variável
num = 0
soma = 0
n = 0

# Laço recuperando os números
while True:
    soma += num
    num = int(input("Digite um número: "))
    if num == 999:
        break
    n += 1
print(f"Você digitou {n} números, a soma dos números é igual a {soma}")

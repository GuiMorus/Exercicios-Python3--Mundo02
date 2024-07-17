# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte
# ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar
# quantas cédulas de cada valor serão entregues.

from random import choice

# Iniciando variáveis
cedula200 = 0
cedula100 = 0
cedula50 = 0
cedula25 = 0
cedula10 = 0
cedula5 = 0
cedula1 = 0

# Mostrando mensagem inicial
print("$$$ 🐍", "-" * 35, "🐍 $$$")
print(" " * 5, f"| $ Boas Vindas ao Caixa e-python $  |")
print("$$$ 🐍", "-" * 35, "🐍 $$$\n")

# Variável resgatando valor a ser sacado
valor = int(input("💰Quanto deseja sacar\nR$"))
saque = valor

# Laço contando as notas
while not saque == 0:
    # Verificando se o saque é maior que mil
    if saque >= 1000:
        cedula = choice([100, 200])

        # Diminuindo saque
        saque -= cedula

        # Somando cédulas
        match cedula:
            case 200:
                cedula200 += 1
            case 100:
                cedula100 += 1

    # Verificando se o saque é maior que 100
    elif 100 <= saque < 1000:
        cedula = choice([100, 50])

        # Diminuindo saque
        saque -= cedula

        # Somando cédulas
        match cedula:
            case 100:
                cedula100 += 1
            case 50:
                cedula50 += 1

    # Verificando se o saque é maior que 50
    elif 50 <= saque < 100:
        cedula = choice([50, 25])

        # Diminuindo saque
        saque -= cedula

        # Somando cédulas
        match cedula:
            case 50:
                cedula50 += 1
            case 25:
                cedula25 += 1

    # Verificando se o saque é maior que 10
    elif 10 <= saque < 50:
        cedula = choice([10, 5])

        # Diminuindo saque
        saque -= cedula

        # Somando cédulas
        match cedula:
            case 10:
                cedula10 += 1
            case 5:
                cedula5 += 1

    # Verificando se o saque é maior que 5
    elif 5 <= saque < 10:
        cedula = choice([1, 5])

        # Diminuindo saque
        saque -= cedula

        # Somando cédula
        match cedula:
            case 5:
                cedula5 += 1
            case 1:
                cedula1 += 1

    # Verificando valores baixos
    elif 1 <= saque < 5:
        # Diminuindo saque
        saque -= 1
        cedula1 += 1

# Mostrando resultado
print("_" * 20)
print("Você recebeu:")

# Verificando cédulas existentes
if cedula200 > 0:
    print("\033[34m" + f"{cedula200}\033[m notas de R$200,00")

if cedula100 > 0:
    print("\033[34m" + f"{cedula100}\033[m notas de R$100,00")

if cedula50 > 0:
    print("\033[34m" + f"{cedula50}\033[m notas de R$50,00")

if cedula25 > 0:
    print("\033[34m" + f"{cedula25}\033[m notas de R$25,00")

if cedula10 > 0:
    print("\033[34m" + f"{cedula10}\033[m notas de R$10,00")

if cedula5 > 0:
    print("\033[34m" + f"{cedula5}\033[m notas de R$5,00")

if cedula1 > 0:
    print("\033[34m" + f"{cedula1}\033[m notas de R$1,00")

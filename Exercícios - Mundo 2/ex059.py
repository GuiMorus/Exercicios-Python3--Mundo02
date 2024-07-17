# Crie um programa que leia dois valores e mostre um menu, seu programa deverá realizar
# a operação solicitada em cada caso.

from time import sleep

# Iniciando variável
op = 0  # op = opção
start = True

# Laço verificando os números e mostrando o menu
while op != 5:
    # Variáveis recolhendo os números
    if start:
        num = float(input("Digite o 1° número: "))
        num2 = float(input("Digite o 2° número: "))
        start = False

    # Menu
    print("\033[m" + ("-" * 30))
    print("Qual operação deseja fazer?")
    print(f"Números: \033[32m{num} | {num2} \033[m")
    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Ver maior")
    print("[4] Novos números")
    print("[5] Sair")
    op = int(input("Opção: "))

    # Verificando opção selecionada
    if op == 1:
        print(f"A soma dos números é igual à \033[32m{num + num2}")
    elif op == 2:
        print(f"A multiplicação dos números é igual à \033[32m{num * num2}")
    elif op == 3:
        maior = [num, num2]
        maior = sorted(maior)
        print(f"O maior número é o \033[32m{maior[1]}")
    elif op == 4:
        start = True
    elif op == 5:
        exit()
    else:
        print("Opção inválida, tente novamente")

    # Esperando para reaparecer o menu
    sleep(1.5)

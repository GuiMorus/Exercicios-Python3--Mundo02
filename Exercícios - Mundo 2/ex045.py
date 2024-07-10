# Crie um programa que faça o computador jogar Jokenpô com você

from random import randint, seed
from datetime import datetime
from time import sleep

game = 1

# Loop do jogo
while game == 1:

    # Mostrando introdução
    print("\033[34m" + "-" * 60)
    print("\033[33m" + "=" * 60)
    print(" *" * 11, "\033[m", "👊JOKENPÔ✋", "\033[33m", " *" * 11)
    print("\033[33m" + "=" * 60)
    print("\033[34m" + "-" * 60, "\033[m")

    # Variável resgatando opção do jogador
    print("JOGADOR")
    print("[ 1 ] 👊 Pedra  -  [ 2 ] ✋ Papel  -  [ 3 ] 🤞 Tesoura  -  [ 0 ] ❌ Sair \n")
    jogador = int(input("Escolha: "))

    # Verificando escolha do jogador
    if jogador == 0:
        exit(0)
    elif jogador < 0 or jogador > 3:
        print("Escolha inválida")
        exit()

    # Animação do JOKENPÔ
    print("\nJO...", end=" ")
    sleep(1)
    print("KE...", end=" ")
    sleep(1)
    print("PÔ! \n")

    # Reiniciando Seed com base na hora
    segundos = datetime.today().second
    milesimos = datetime.today().microsecond
    seed(milesimos * segundos)

    # Desenhando jogador vs python
    python = randint(1, 3)
    jogada = {'1': '👊', '2': '✋', '3': '🤞'}

    print(f"JOGADOR {jogada[str(jogador)]}  vs  {jogada[str(python)]} PYTHON")

    # Mostrando o vencedor do jogo
    if python == jogador:
        print("\033[33m" + "EMPATE TÉCNICO!")

    elif jogador == 1 and python == 3:
        print("\033[32m" + "JOGADOR VENCEU!")
    elif python == 1 and jogador == 3:
        print("\033[34m" + "O PYTHON TE VENCEU!")

    elif jogador == 2 and python == 1:
        print("\033[32m" + "JOGADOR VENCEU!")
    elif python == 2 and jogador == 1:
        print("\033[34m" + "O PYTHON TE VENCEU!")

    elif jogador == 3 and python == 2:
        print("\033[32m" + "JOGADOR VENCEU!")
    elif python == 3 and jogador == 2:
        print("\033[34m" + "O PYTHON TE VENCEU!")

    # Escolhendo reiniciar ou sair do jogo
    print("\n\033[m" + "[ 1 ] Sim   -    [ 2 ] Não")
    game = int(input("Jogar novamente?: "))

else:
    exit()

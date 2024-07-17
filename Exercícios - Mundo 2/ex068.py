# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
# quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou
# no final do jogo.

from random import randint

# Variável Inicial
vitorias = 0

# Introdução
print("\033[31m")
print("=" * 20, "GAME", "=" * 20)
print("\033[33m")
print("#~" + "~" * 15, end="PAR OU ÍMPAR")
print("~" * 15 + "~#")
print("\033[m")

# Laço mantendo o jogo
while True:
    # Recolhendo jogada
    print("-" * 30)
    print("[ P ] Par   -   [ I ] Ímpar")
    jogador = input("Selecione a opção: ").lower().strip()

    # Tratando a jogada
    jogador = jogador.replace("ímpar", "i")
    jogador = jogador.replace("impar", "i")
    jogador = jogador.replace("par", "p")

    # Verificando seleção correta
    if jogador == 'p' or jogador == 'i':

        # Recolhendo número da jogada
        num = input("Escolha um número(1 à 10): ")

        # Verificando type da jogada
        if num.isnumeric():
            num = int(num)

            # Verificando se a jogada esta entre 1 e 10
            if 0 < num <= 10:
                # Gerando número aleatório
                python = randint(1, 10)
                print(f"Python: {python}")

                # Condição verificando resultado
                resultado = (num + python) % 2

                if jogador == 'p' and resultado == 0:
                    print("Jogador" + "\033[32m", "GANHOU" + "\033[m", "esta rodada")
                    vitorias += 1
                elif jogador == 'i' and resultado == 1:
                    print("Jogador" + "\033[32m", "GANHOU" + "\033[m", "esta rodada")
                    vitorias += 1
                else:
                    print("\n" + "~x~" * 12)
                    print("Jogador" + "\033[31m", "PERDEU" + "\033[m", "esta rodada")
                    break

# Finalização do Game
print("Você teve", f"\033[32m{vitorias} vitorias\033[m", "consecutivas")
print("\033[31m")
print("=" * 46)
print("=" * 18, "END GAME", "=" * 18)
print("=" * 46)
print("\033[33m")

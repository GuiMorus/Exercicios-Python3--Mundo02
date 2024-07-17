# Melhore o jogo do DESAFIO 028 onde o computador vai escolher um número de 0 a 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
# palpites foram necessários para vencer.

from random import randint

# Iniciando variável
palpite = -1
tentativas = 0

# Gerando número aleatório
python = randint(0, 10)
print("Tente adivinhar um número que eu escolhi de 0 à 10")

# Laço da escolha do usuário
while palpite != python:
    palpite = int(input("Palpite: "))
    tentativas += 1

    # Mostrando dica para o usuário
    if palpite > python:
        print("tente um pouco menos")
    elif palpite < python:
        print("tente um pouco mais")

# Mostrando mensagem de acerto e tentativas
print(f"YUUUP!!! você acertou! era exatamente o {python} que eu escolhi")
if tentativas == 1:
    print("👏VOCÊ ACERTOU DE PRIMEIRA👏")
else:
    print(f"Você acertou depois de {tentativas} tentativas")

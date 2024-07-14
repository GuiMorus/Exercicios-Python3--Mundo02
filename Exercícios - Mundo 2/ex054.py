# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
# pessoas ainda não atingiram a maioridade e quantas já são maiores

from datetime import datetime

#Iniciando Variável
atual = datetime.today().year
maiores = 0
menores = 0

# Ciclo resgatando a idade das pessoas
for c in range(1, 8):
    ano = int(input(f"Em que ano nasceu a {c}° pessoa(0000): "))
    if atual - ano >= 21:
        maiores += 1
    else:
        menores += 1

# Mostrando os maiores e menores de idade
print(f"Das 7 pessoas, {maiores} são maioridade e {menores} são menores")

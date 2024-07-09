# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou
# do tempo de se apresentar pro alistamento. Seu programa também deverá mostrar o tempo que falta
# ou que passou do prazo.

from datetime import datetime

# Mensagem de entrada
print("\033[32m", "-=" * 15, " 💂‍♂️ BEM VINDO AO ALISTAMENTO VIRTUAL 💂‍♂️ ", "-=" * 15)
print("O \033[32mB\033[34mr\033[33ma\033[ms\033[32mi\033[34ml \033[32mprecisa de você, soldado!", end="")
print("\033[m")
# Variável resgatando o ano de nascimento
ano = int(input("Em que ano você nasceu: "))
mes = int(input("Em que mês(número): "))

# Mostrando a condição de alistamento
ano_atual = datetime.today().year
mes_atual = datetime.today().month
idade = ano_atual - ano

if mes_atual - mes < 0:     # Reformatando idade a depender do mês
    idade -= 1

if idade == 18:
    print("Você está com 18 anos")
    print("Está na hora de se apresentar ao Serviço Militar")
elif idade < 18:
    dif = 18 - idade
    print(f"Você está com {idade} anos")
    print(f"Você tem que se apresentar ao alistamento em {ano_atual + dif}")
elif idade > 18:
    dif = idade - 18
    print(f"Você já tem {idade} anos")
    print(f"Você tinha que se alistar no ano de {ano_atual - dif}, apresente-se ao alistamento mais perto")

print("\033[32m", "-=" * 17, " 💂‍ SERVIÇO DE ALISTAMENTO 💂‍ ", "-=" * 18)

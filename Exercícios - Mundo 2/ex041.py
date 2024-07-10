# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um
# atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: Mirim     Até 14 anos: Infantil       Até 19 anos: Junior
# Até 25 anos: Sênior   Acima: Master

from datetime import datetime

# Variáveis recolhendo o nome e a idade
nome = input("Qual o seu nome: ").title()
ano = int(input("Em que ano você nasceu: "))

# Mostrando a categoria de natação
idade = datetime.today().year - ano

print(f"Boas vindas a Confederação Nacional de Natação, {nome}!")

if 0 < idade <= 9:
    print("Sua categoria é Mirim")
elif 9 < idade <= 14:
    print("Sua categoria é Infantil")
elif 14 < idade <= 19:
    print("Sua categoria é Junior")
elif 19 < idade <= 25:
    print("Sua categoria é Sênior")
elif idade > 25:
    print("Sua categoria é Master")
else:
    print("Não conseguimos computar sua idade")
    print("TENTE NOVAMENTE")

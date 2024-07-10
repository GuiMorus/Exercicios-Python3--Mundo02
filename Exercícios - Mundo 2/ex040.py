# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem
# no final, de acordo com a média atingida
# Média abaixo de 5: REPROVADO
# Média entre 5 e 6.9: RECUPERAÇÃO
# Média 7 ou superior: APROVADO

# Variáveis resgatando as notas
nota = float(input("Qual a sua 1° Nota: "))
nota2 = float(input("Qual a sua 2° Nota: "))
media = (nota + nota2) / 2

# Mostrando a mensagem pro aluno
if media < 5:
    print(f"Sua média foi {media:.1f}, você está REPROVADO")
elif 5 <= media <= 6.9:
    print(f"Sua média foi {media:.1f}, você está de RECUPERAÇÃO")
elif media >= 7:
    print(f"PARABENS!! Sua média foi {media:.1f}, você está APROVADO")

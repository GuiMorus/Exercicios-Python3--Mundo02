# Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior
# e o menor peso lidos

#Iniciando variável
pessoas = []

# Ciclo resgatando o peso das pessoas
for c in range(1, 6):
    peso = float(input(f"Qual o peso da {c}° pessoa(kg): "))
    pessoas.append(peso)

# Mostrando o maior peso para o menor
pessoas = sorted(pessoas)
pessoas.reverse()
print("Pesos do maior para o menor")
print(pessoas)

# Refaça o DESAFIO 051, resgatando o primeiro termo e a razão de uma PA, mostrando os
# 10 primeiros termos da progressão usando a estrutura while.

# Variáveis resgatando os valores
termo = int(input("Qual o primeiro termo da PA: "))
r = int(input("Informe a razão entre os termos: "))     # r = razão
c = 1     # c = contador
termos = []

# Laço calculando a PA
while c <= 10:
    termos.append(termo)
    termo += r
    c += 1

# Mostrando o resultado da PA
print("Progressão aritmética")
print(f"Primeiro termo: {termos[0]} | razão: {r}")
print(termos)

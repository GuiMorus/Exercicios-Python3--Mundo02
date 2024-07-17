# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais
# alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos
# REFIZ

# Iniciando variáveis
termos = []
c = 1   # c = contador
limite = 10

# Variáveis resgatando valores
termo = int(input("Digite o primeiro termo: "))
r = int(input("Qual a razão da sua PA: "))  # r = razão

# Primeira mensagem
print("Os 10 primeiros termos são:")

# Laço calculando as PAs
while c <= limite != 0:
    termos.append(termo)
    termo += r
    c += 1

    # Condições após 10 termos
    if c > limite:
        print(termos)
        outros = int(input("Quantos termos quer mostrar a mais? "))
        limite += outros  # Adicionando mais termos

        if outros == 0:
            limite = 0

# Mostrando mensagem final
print(f"PA finalizada. sua progressão tem {len(termos)} termos ")

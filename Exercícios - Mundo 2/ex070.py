# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
# perguntar se o usuário vai continuar. No final mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1.000,00.
# C) Qual é o nome do produto mais barato.

# Iniciando Variáveis
carrinho = []
continuar = ''
total = 0
caros = 0
barato = 0
nome_barato = ''

# Mostrando mensagem inicial
print("💲" * 20)
print("LOJA ONLINE - SAARAZON")
print("💲" * 20)

# Laço das compras
while True:
    # Verificando continuidade do programa
    if continuar == 'n':
        break
    continuar = ''

    # Cadastrando produtos no carrinho
    print("")   # pulando linha
    produto = str(input("🛒Produto: ").title())
    valor = float(input("Valor: R$").replace(",", "."))
    carrinho.append([produto, valor])

    # Verificando primeiro produto
    if barato <= 0:
        nome_barato = carrinho[0][0]
        barato = carrinho[0][1]

    # Verificando se o usuário deseja continuar
    while continuar != 's' and continuar != 'n':
        continuar = str(input("Deseja continuar comprando [S/N]: "))

        # Tratando informação
        continuar = continuar.lower().strip()
        continuar = continuar.replace('sim', 's')
        continuar = continuar.replace('não', 'n')
        continuar = continuar.replace('nao', 'n')

# Repetição verificando o total dos produtos
for c in carrinho:
    total += c[1]

# Repetição verificando produtos mais caro
for c in carrinho:
    if c[1] >= 1000:
        caros += 1

# Repetição verificando o nome do produto mais barato
for c in carrinho:
    if c[1] <= barato:
        nome_barato = c[0]
        barato = c[1]

# Mostrando resultados
print("\n\033[32m" + "=" * 50, "\033[m")
print("🛒Carrinho finalizado com sucesso")
print(f"A) O total da compra: R${total:.2f}")
print(f"B) Há {caros} produtos que custam mais de R$1.000,00")
print(f"C) O produto {nome_barato} foi o mais barato, custando R${barato:.2f}")

# Elabore um programa que calcule o valor a ser pago por um produto, considerando
# o seu preço normal e condição de pagamento:
# à vista(dinheiro/cheque): 10% de desconto     à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal             3x ou mais no cartão: 20% de juros

# Variáveis resgatando o valor e forma de pagamento
print("-" * 50)
compra = float(input("Qual o valor total da compra: R$").replace(",", "."))
print("-" * 50)
print("Qual a forma de pagamento?")
print("[ 1 ] - Dinheiro/Cheque")
print("[ 2 ] - Débito")
print("[ 3 ] - 2x no Crédito")
print("[ 4 ] - 3x ou mais no Crédito")

pagamento = int(input("Digite a opção: "))
print("-" * 50)

# Mostrando a porcentagem do valor conforme a forma de pagamento
if pagamento == 1:
    valor = compra - (compra * 0.10)
    print("Você recebeu 10% de desconto na sua compra!")
elif pagamento == 2:
    valor = compra - (compra * 0.05)
    print("Você recebeu 5% de desconto na sua compra!")
elif pagamento == 3:
    valor = compra
    print(f"Sua compra ficou em 2x de R${(valor / 2):.2f} sem juros!")
elif pagamento == 4:
    valor = compra * 1.20
    vezes = int(input("Quantas Parcelas: "))
    print(f"Sua compra ficou em {vezes}x de R${(valor / vezes):.2f}")
    print("COM 20% DE JUROS no total da compra")
else:
    valor = "ERROR"
    print("houve um erro na forma de pagamento".upper())
    print("TENTE NOVAMENTE!")
    exit()

# Mostrando o total a pagar conforme a forma de pagamento
valor = str(f"{valor:.2f}")     # Formatando o valor em String
valor = valor.replace(".", ",")     # Substituindo . por ,
print("\033[32m" + f"Total: R${valor}" + "\033[m")

print("=" * 50)

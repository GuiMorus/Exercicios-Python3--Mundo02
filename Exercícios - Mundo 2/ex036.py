# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa. o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.

# Variáveis resgatando valor da casa e salário
casa = float(input("Qual o valor da casa que deseja comprar: R$"))
salario = float(input("Qual o seu salário: R$"))
anos = int(input("Quer pagar em quantos anos: "))

# Mostrando ao usuário as condições de pagamento
parcela = anos * 12
mensal = casa / parcela

if mensal > (salario * 0.30):
    print("EMPRÉSTIMO NEGADO: As parcelas excedem 30% do seu salário")
else:
    print(f"Parcela aprovada, você pagará {parcela:.0f} parcelas de R${mensal:.2f} por mês")

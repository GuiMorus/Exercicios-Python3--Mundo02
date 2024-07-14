# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, desta vez
# utilizando um laço for

# Variável resgatando o valor para tabuada
print("=" * 15, "Tabuada Maker 2000", "=" * 15)
num = int(input("Digite o número: "))

# Repetindo número escolhido desenhando uma tabuada
for c in range(0, 11):
    # Mostrando tabuada
    resultado = num * c
    print(f"{num}", "x", f"{c}", end=" ")
    print(f"= {resultado}")

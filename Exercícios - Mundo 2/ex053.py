# Crie um programa que leia uma frase qualquer e diga se ela é um políndromo,
# desconsiderando os espaços

# Iniciando variável
reverso = ""

# Variável resgatando a frase
frase = str(input("Digite uma frase: "))
frase = frase.lower()

# Revertendo frase
frase = frase.split()
frase.reverse()
tamanho = len(frase)

# Lendo da primeira lista até a ultima
for c in range(0, tamanho):
    palavra = frase[c]  # Pegando a palavra de cada indice da lista frase
    tp = len(palavra) - 1   # tp = tamanho palavra

    # Lendo e mostrando da ultima letra à primeira
    for n in range(tp, -1, -1):
        # Mostrando palavra revertida e junta
        reverso = reverso + palavra[n]

# Verificando se é um políndromo
frase.reverse()
if "".join(frase) == reverso:
    print("Esta frase é um políndromo")
else:
    print("Essa é uma frase comum")

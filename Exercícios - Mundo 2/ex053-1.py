# Crie um programa que leia uma frase qualquer e diga se ela é um políndromo,
# desconsiderando os espaços
# REFEITO SEM O ERRO DA CAIXA DA PASTA DE DENTE | toothpaste box's error

# Variável resgatando a frase
frase = input("Digite uma frase: ")
frase = frase.lower().replace(" ", "")

# Revertendo a frase
tamanho = len(frase) - 1
reverso = ""
for c in range(tamanho, -1, -1):
    reverso = reverso + frase[c]

# Verificando se é a frase é um políndromo
if frase == reverso:
    print("A frase acima é um políndromo")
else:
    print("Essa é uma palavra comum")

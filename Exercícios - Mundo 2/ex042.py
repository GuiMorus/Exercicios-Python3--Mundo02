# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de
# triângulo será formado:
# Equilátero: Todos os lados iguais     Isósceles: Dois lados iguais      Escaleno: Todos os lados diferentes

# Variáveis resgatando os segmentos
a = float(input("Qual o tamanho do primeiro segmento: "))
b = float(input("Qual o tamanho do segundo segmento: "))
c = float(input("Qual o tamanho do terceiro segmento: "))

# Verificando segmentos para triângulo
segmentos = sorted([a, b, c])

if segmentos[2] < segmentos[0] + segmentos[1]:
    #Verificando o tipo de triângulo
    if a == b == c:
        tipo = "Equilátero"
    elif a == b or a == c or b == c:
        tipo = "Isósceles"
    elif a != b != c:
        tipo = "Escaleno"

    # Mostrando ao usuário o tipo de triângulo
    print(f"Esses segmentos formam um triângulo {tipo}.")
else:
    print("Estes segmentos não formam um triângulo")

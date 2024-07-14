# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
# 1) A média de idade do grupo
# 2) Qual é o nome do homem mais velho
# 3) Quantas mulheres tem menos de 20 anos

# Iniciando Variáveis
pessoas = []
media = 0
maior_idade = 0
indice_idade = 0
mulheres = 0
homem = False

# Ciclo resgatando as informações das pessoas
for c in range(1, 5):
    nome = str(input(f"Qual o nome da {c}° pessoa: "))
    idade = int(input("Qual a idade: "))
    print("[ 1 ] Masculino | [ 2 ] Feminino | [ 3 ] Outros")
    sexo = int(input("Qual o sexo: "))
    if sexo == 1:
        homem = True

    # Criando lista com as informações
    pessoas.append([nome, idade, sexo])

# Mostrando a média de idade do grupo
for c in range(0, 4):
    media += pessoas[c][1]

media = round(media / 4)
print(f"A idade média do grupo é de {media} anos")

# Mostrando o homem mais velho
for c in range(0, 4):
    if pessoas[c][1] > maior_idade:
        maior_idade = pessoas[c][1]
        indice_idade = c

if homem:
    print(f"O homem mais velho é o {pessoas[indice_idade][0].title()} e ele tem {maior_idade} anos")

# Mostrando quantas mulheres tem menos de 20 anos
for c in range(0, 4):
    if pessoas[c][1] <= 20 and pessoas[c][2] == 2:
        mulheres += 1

print(f"Há {mulheres} mulheres com menos de 20 anos")
